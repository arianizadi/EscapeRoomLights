import asyncio

from wled import WLED

Green = (0, 255, 0, 255)
Red = (255, 0, 0, 255)

On = 255
Off = 0

Sleep = 1


async def room_one(mode: str) -> None:
    async with WLED("192.168.1.122") as led:
        match mode:
            case "green":
                await led.segment(
                    0,
                    start=0,
                    stop=198,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )
            case "red":
                await led.segment(
                    0,
                    start=0,
                    stop=198,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )
            case "off":
                await led.segment(
                    0,
                    start=0,
                    stop=198,
                    brightness=Off,
                    effect="Solid",
                )


async def room_two(mode: str) -> None:
    match mode:
        case "green":
            async with WLED("192.168.1.122") as led:
                await led.segment(
                    0,
                    start=127,
                    stop=291,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )

                await led.segment(
                    1,
                    start=640,
                    stop=750,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )

            async with WLED("192.168.1.115") as led:
                await led.segment(
                    0,
                    start=55,
                    stop=150,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )

        case "red":
            async with WLED("192.168.1.122") as led:
                await led.segment(
                    0,
                    start=127,
                    stop=291,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )

                await led.segment(
                    1,
                    start=640,
                    stop=750,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )

            async with WLED("192.168.1.115") as led:
                await led.segment(
                    0,
                    start=55,
                    stop=150,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )

        case "off":
            async with WLED("192.168.1.122") as led:
                await led.segment(
                    0,
                    start=127,
                    stop=291,
                    brightness=Off,
                    effect="Solid",
                )

                await led.segment(
                    1,
                    start=640,
                    stop=750,
                    brightness=Off,
                    effect="Solid",
                )

            async with WLED("192.168.1.115") as led:
                await led.segment(
                    0,
                    start=55,
                    stop=150,
                    brightness=Off,
                    effect="Solid",
                )


async def room_three(mode: str) -> None:
    match mode:
        case "green":
            async with WLED("192.168.1.115") as led:
                await led.segment(
                    0,
                    start=57,
                    stop=406,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )

            async with WLED("192.168.1.133") as led:
                await led.segment(
                    0,
                    start=700,
                    stop=750,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )
        case "red":
            async with WLED("192.168.1.115") as led:
                await led.segment(
                    0,
                    start=57,
                    stop=406,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )

            async with WLED("192.168.1.133") as led:
                await led.segment(
                    0,
                    start=650,
                    stop=750,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )

        case "off":
            async with WLED("192.168.1.115") as led:
                await led.segment(
                    0,
                    start=57,
                    stop=406,
                    color_primary=Red,
                    brightness=Off,
                    effect="Solid",
                )

            async with WLED("192.168.1.133") as led:
                await led.segment(
                    0,
                    start=650,
                    stop=750,
                    color_primary=Red,
                    brightness=Off,
                    effect="Solid",
                )


async def room_four(mode: str) -> None:
    async with WLED("192.168.1.133") as led:
        match mode:
            case "green":
                await led.segment(
                    0,
                    start=290,
                    stop=608,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )
            case "red":
                await led.segment(
                    0,
                    start=290,
                    stop=608,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )
            case "off":
                await led.segment(
                    0,
                    start=290,
                    stop=608,
                    brightness=Off,
                    effect="Solid",
                )


async def room_five(mode: str) -> None:
    match mode:
        case "green":
            async with WLED("192.168.1.133") as led:
                await led.segment(
                    0,
                    start=64,
                    stop=285,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )
                await led.segment(
                    1,
                    start=616,
                    stop=701,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )
            async with WLED("192.168.1.115") as led:
                await led.segment(
                    0,
                    start=408,
                    stop=750,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )
        case "red":
            async with WLED("192.168.1.133") as led:
                await led.segment(
                    0,
                    start=64,
                    stop=285,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )
                await led.segment(
                    1,
                    start=616,
                    stop=701,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )
            async with WLED("192.168.1.115") as led:
                await led.segment(
                    0,
                    start=408,
                    stop=750,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )
        case "off":
            async with WLED("192.168.1.133") as led:
                await led.segment(
                    0,
                    start=64,
                    stop=285,
                    brightness=Off,
                    effect="Solid",
                )
                await led.segment(
                    1,
                    start=616,
                    stop=701,
                    brightness=Off,
                    effect="Solid",
                )
            async with WLED("192.168.1.115") as led:
                await led.segment(
                    0,
                    start=408,
                    stop=750,
                    brightness=Off,
                    effect="Solid",
                )


async def room_six(mode: str) -> None:
    match mode:
        case "green":
            async with WLED("192.168.1.122") as led:
                await led.segment(
                    0,
                    start=292,
                    stop=640,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )
        case "red":
            async with WLED("192.168.1.122") as led:
                await led.segment(
                    0,
                    start=292,
                    stop=640,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )
        case "off":
            async with WLED("192.168.1.122") as led:
                await led.segment(
                    0,
                    start=292,
                    stop=640,
                    brightness=Off,
                    effect="Solid",
                )


async def all_red() -> None:
    async with WLED("192.168.1.122") as led:
        await led.segment(
            0,
            start=0,
            stop=750,
            color_primary=Red,
            brightness=On,
            effect="Blink",
            speed=200,
        )

    async with WLED("192.168.1.115") as led:
        await led.segment(
            0,
            start=0,
            stop=750,
            color_primary=Red,
            brightness=On,
            effect="Blink",
            speed=200,
        )

    async with WLED("192.168.1.133") as led:
        await led.segment(
            0,
            start=0,
            stop=750,
            color_primary=Red,
            brightness=On,
            effect="Blink",
            speed=200,
        )


async def all_off() -> None:
    async with WLED("192.168.1.122") as led:
        await led.segment(
            0,
            start=0,
            stop=750,
            brightness=Off,
        )

    async with WLED("192.168.1.115") as led:
        await led.segment(
            0,
            start=0,
            stop=750,
            brightness=Off,
        )

    async with WLED("192.168.1.133") as led:
        await led.segment(
            0,
            start=0,
            stop=750,
            color_primary=Red,
            brightness=Off,
        )


async def reset_segments() -> None:
    async with WLED("192.168.1.122") as led:
        await led.segment(
            0,
            start=0,
            stop=1,
        )
        await led.segment(
            1,
            start=2,
            stop=3,
        )

        await led.segment(
            3,
            start=4,
            stop=5,
        )

    async with WLED("192.168.1.115") as led:
        await led.segment(
            0,
            start=0,
            stop=1,
        )
        await led.segment(
            1,
            start=2,
            stop=3,
        )

        await led.segment(
            3,
            start=4,
            stop=5,
        )

    async with WLED("192.168.1.133") as led:
        await led.segment(
            0,
            start=0,
            stop=1,
        )
        await led.segment(
            1,
            start=2,
            stop=3,
        )

        await led.segment(
            3,
            start=4,
            stop=5,
        )

    await all_off()


async def all_color(color: str) -> None:
    await reset_segments()
    match color:
        case "green":
            async with WLED("192.168.1.133") as led:
                # await led.sync(send=True)
                await led.segment(
                    0,
                    start=295,
                    stop=615,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )
                await led.segment(
                    1,
                    start=705,
                    stop=750,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )
            async with WLED("192.168.1.122") as led:
                # await led.sync(send=True)
                await led.segment(
                    0,
                    start=0,
                    stop=750,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )
            async with WLED("192.168.1.115") as led:
                # await led.sync(send=True)
                await led.segment(
                    0,
                    start=0,
                    stop=400,
                    color_primary=Green,
                    brightness=On,
                    effect="Solid",
                )
        case "red":
            async with WLED("192.168.1.133") as led:
                # await led.sync(send=True)
                await led.segment(
                    0,
                    start=0,
                    stop=750,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )
            async with WLED("192.168.1.122") as led:
                # await led.sync(send=True)
                await led.segment(
                    0,
                    start=0,
                    stop=750,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )
            async with WLED("192.168.1.115") as led:
                # await led.sync(send=True)
                await led.segment(
                    0,
                    start=0,
                    stop=750,
                    color_primary=Red,
                    brightness=On,
                    effect="Blink",
                    speed=200,
                )
        case "off":
            async with WLED("192.168.1.133") as led:
                # await led.sync(send=True)
                await led.segment(
                    0,
                    start=0,
                    stop=750,
                    brightness=Off,
                )
            async with WLED("192.168.1.122") as led:
                # await led.sync(send=True)
                await led.segment(
                    0,
                    start=0,
                    stop=750,
                    brightness=Off,
                )
            async with WLED("192.168.1.115") as led:
                # await led.sync(send=True)
                await led.segment(
                    0,
                    start=0,
                    stop=750,
                    brightness=Off,
                )


async def main() -> None:
    valid_options = ["1", "2", "3", "4", "5", "6", "r", "g", "o", "s"]
    valid_colors = ["green", "red", "off"]
    option = ""
    while option != "q":
        print("1 - Entrance")
        print("2 - Riddles and Phising")
        print("3 - Safe and Drone")
        print("4 - Lockpicking")
        print("5 - Invisible Ink/Cipher Wheel")
        print("6 - USB Tampering / Social Engineering")
        print("r - Whole Room")

        print("q - Quit")
        option = input("Enter room number: ")

        if option == "q":
            break

        if option not in valid_options:
            print("Invalid room number")
            continue

        if option == "r":
            color = input("Enter color (green, red, off): ")

            if color not in valid_colors:
                print("Invalid color")
                continue

        await reset_segments()

        match option:
            case "1":
                await room_one("green")
            case "2":
                await room_two("green")
            case "3":
                await room_three("green")
            case "4":
                await room_four("green")
            case "5":
                await room_five("green")
            case "6":
                await room_six("green")
            case "r":
                await all_color(color)
            case _:
                print("Invalid room number")

        print("\033c", end="")


if __name__ == "__main__":
    asyncio.run(main())
