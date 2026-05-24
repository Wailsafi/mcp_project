import os 
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters, client
import asyncio

# path teh the Mcp server  script 
mcp_server_script_path = os.path.join(os.path.dirname(__file__), 'main.py')

print(mcp_server_script_path)
server_parameters = StdioServerParameters(command="python", args=[str(mcp_server_script_path)], env={})

# Create a client Session 

async def main():
    async with stdio_client(server_parameters) as (read,write):
        async with  ClientSession(read,write) as Session:
            
            await Session.initialize()
            tools= await Session.list_tools()
            print("Available tools:", tools)
            processed_data=await Session.call_tool("processData", {"data": "sample data to process"})
            print("Processed Data:", processed_data)
            

if __name__ == "__main__":
    asyncio.run(main())

            

            





