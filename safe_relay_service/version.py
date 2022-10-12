__version__ = "v4.1.15-pre-ca2abd4-1-g2dc0152"
__version_info__ = tuple(
    [
        int(num) if num.isdigit() else num
        for num in __version__.replace("-", ".", 1).split(".")
    ]
)
