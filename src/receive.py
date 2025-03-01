"""import asyncio

import aio_pika


async def process_message(
    message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    async with message.process():
        print("processing message")
        print(message.body)
        await asyncio.sleep(1)


async def main_receive() -> None:
    connection = await aio_pika.connect_robust(
        #"amqp://default_user_76OfnLbsBcbM1bz9WgU:fqg-oAhmS8jJG0HCxib6Ub_DBFQ0IEcS@hello-world/",
        "amqp://guest:guest@127.0.0.1/",
    )

    queue_name = "hello"

    # Creating channel
    channel = await connection.channel()

    # Maximum message count which will be processing at the same time.
    await channel.set_qos(prefetch_count=100)

    # Declaring queue
    queue = await channel.declare_queue(queue_name, auto_delete=False)

    await queue.consume(process_message)

    try:
        # Wait until terminate
        await asyncio.Future()
    finally:
        await connection.close()


if __name__ == "__main__":
    asyncio.run(main_receive())"""