import logging

from openai import AsyncOpenAI

from bot.src.utils.config import settings

logger = logging.getLogger()


client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.DEEPSEEK_API_KEY,
)

async def ai_generate(prompt: str):
    completion = await client.chat.completions.create(
      model="deepseek/deepseek-chat-v3-0324",
      messages=[
        {
          "role": "user",
          "content": prompt
        }
      ]
    )
    logger.info(f'Total tokens {completion.usage.total_tokens}')
    return completion.choices[0].message.content
