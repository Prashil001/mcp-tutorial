import os
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters, client
import asyncio

mcp_server_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_first_mcp_server_stdio.py")
print(f"Starting MCP server from script: {mcp_server_script}")

server_params = StdioServerParameters(
    command = "python",
    args = [mcp_server_script],
    env = {}
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:", tools)

            result =  await session.call_tool("process", arguments={"data": "Sample data fetched from remote source."})
            print("Tool execution result:", result)

if __name__ == "__main__":
    asyncio.run(main())