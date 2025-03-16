import asyncio
from langchain_ollama import ChatOllama
from browser_use import Agent

prompt=""""

"""
async def run_search():
	agent=Agent(
		task=input("prompt:"),	
	llm = ChatOllama(model='qwen2.5:3b',
	num_ctx=32000,
	),
	max_actions_per_step=3,
	)


	result=await agent.run(max_steps=15)
	return result

async def main():
	result=await run_search()
	print("\n\n",result)


if __name__ == '__main__':
	asyncio.run(main())