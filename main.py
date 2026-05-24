from fastmcp import FastMCP

mcp=FastMCP()

@mcp.tool
def  fetchData():
    '''use this took to fetch data from a database'''
    return {"data": "this is your data"}

@mcp.tool
def processData(data):
    '''use this tool to process data'''
    return {"processed_data": f"this is your processed data: {data}"}

mcp.run()