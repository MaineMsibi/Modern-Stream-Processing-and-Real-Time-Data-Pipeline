import random
import json 
import asyncio
import datetime 
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from datetime import timezone, timedelta

# Azure Event Hub settings
# connection_str = 'connection_string_here'
# event_hub_name = 'event_hub_name_here'

# Sample values
card_types = ['Visa', 'MasterCard', 'Amex', 'Discover']
transaction_types = ['Purchase', 'Withdrawal', 'Deposit', 'Transfer']
currencies = ['USD', 'EUR', 'GBP', 'INR', 'ZAR']
locations = ['New York', 'London', 'Berlin', 'Mumbai', 'Tokyo', 'Sydney', 'Cape Town']



def generate_transaction():
    # Date conversion to SAST (UTC+2)
    sast_time = datetime.datetime.utcnow().replace(tzinfo=timezone.utc) + timedelta(hours=2)
    rand = random.random()
    if rand < 0.2:
        atm_id = f"ATM-{random.randint(100,999)}"
    elif rand < 0.6:
        atm_id = "POS"
    else:
        atm_id = "Online"
    return {
        
        "transaction_id": f"TXN{random.randint(1000000, 9999999)}",
        "timestamp":sast_time.isoformat(),
        "card_number": f"{random.randint(4000,4999)} **** **** {random.randint(1000,9999)}",
        "card_type": random.choice(card_types),
        "transaction_type": random.choice(transaction_types),
        "amount": round(random.uniform(5.0, 1000000.0), 2),
        "currency": random.choice(currencies),
        "location": random.choice(locations),
        "status": random.choice(["Approved", "Declined", "Pending"]),
        "atm_id": atm_id
    }

async def main():
    producer = EventHubProducerClient.from_connection_string(
        conn_str=connection_str,
        eventhub_name=event_hub_name
    )

    try:
        print("Streaming live banking transactions...")
        while True:
            data = generate_transaction()
            event_data = EventData(json.dumps(data))

            batch = await producer.create_batch()
            batch.add(event_data)
            await producer.send_batch(batch)

            print(f"Sent: {data}")
            await asyncio.sleep(10)
    except (KeyboardInterrupt, asyncio.CancelledError):
        print("Stopped by user.")
    finally:
        await producer.close()

if __name__ == "__main__":
    asyncio.run(main())
