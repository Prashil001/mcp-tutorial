from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool
async def fetch_http():
    """
    Fetches data from a remote source.
    """
    # Simulate fetching data
    return {"data": "Sample data fetched from remote source."}

@mcp.tool
async def process_http(data: str):
    """
    Processes the fetched data.
    """
    # Simulate processing data
    processed_data = data.upper()
    return {"processed_data": processed_data}

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8050)