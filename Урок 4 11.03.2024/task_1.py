def split_text(text: str) -> None:
    text = text.split()
    max_len = len(max(text, key=len))

    for i, item in enumerate(sorted(text), 1):
        print(f'{i}. {item:>{max_len}}')


split_text('sdfdsgdfh dfghdf hgdfghfgh fghgfh fgh zfghfgh fghfg hgfhf fghfghfghfhfgh')
