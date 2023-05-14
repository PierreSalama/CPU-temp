import wmi
import win10toast
import time

import discord

def get_cpu_temp():
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    for sensor in temperature_infos:
        if sensor.SensorType == 'Temperature':
            if "CPU CCD #1" in sensor.Name:
                return sensor.Value


toaster = win10toast.ToastNotifier()



# Set the Discord API token
TOKEN = "ur token"

# Create a Discord client with the required intents
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# Set the ID of the text channel you want to send the message to
channel_id = ur channel ID

# This event will be called when the bot is ready
@client.event
async def on_ready():
    # Get the text channel object
    channel = client.get_channel(channel_id)

    # Send a message to the text channel
    while True:
        if get_cpu_temp() > 85:
            await channel.send("CPU OVER HEATING")
            time.sleep(10)

# Start the Discord client
client.run(TOKEN)