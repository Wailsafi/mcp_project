from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os 

path_to_mcp_server= os.path.join(os.path.abspath(os.path.dirname(__file__)), "main.py")
print(path_to_mcp_server)
path_to_python=os.path.join(os.path.abspath(os.path.dirname(__file__)), ".venv/bin/python")
print(path_to_python)


async def main():
    client = MultiServerMCPClient(

    {
        "data_fetch_mcp":{
            'transport':"stdio",
            "command": path_to_python,
            "args": [path_to_mcp_server],
            "env": {}
    }}
)
# list tools 
    tools= await client.get_tools()
    print("Available tools:", tools)
if __name__ == "__main__":
    asyncio.run(main())   

