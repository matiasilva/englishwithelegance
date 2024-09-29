import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Cloudflare API credentials
ZONE_ID = os.getenv('CLOUDFLARE_ZONE_ID')
API_TOKEN = os.getenv('CLOUDFLARE_API_TOKEN')
RECORD_NAME = os.getenv('CLOUDFLARE_RECORD_NAME')

def get_public_ip():
    """Get the current public IP address."""
    response = requests.get('https://api.ipify.org')
    return response.text

def update_dns_record(ip):
    """Update the DNS record in Cloudflare."""
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Get existing DNS records
    response = requests.get(url, headers=headers)
    records = response.json()['result']
    
    # Find the record we want to update
    record_id = None
    for record in records:
        if record['name'] == RECORD_NAME:
            record_id = record['id']
            break
    
    if not record_id:
        print(f"Record {RECORD_NAME} not found.")
        return
    
    # Update the record
    update_url = f"{url}/{record_id}"
    data = {
        "type": "A",
        "name": RECORD_NAME,
        "content": ip,
        "ttl": 1,  # 1 = automatic
        "proxied": False
    }
    
    response = requests.put(update_url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f"Successfully updated IP to {ip}")
    else:
        print(f"Failed to update IP. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    current_ip = get_public_ip()
    update_dns_record(current_ip)