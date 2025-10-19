rule test_wachizungu
{
    meta:
        author = "@wachizungu"
        info = "Part of test"

    strings:
        $a1 = "DELAY"
        $a2 = "GUI r"
        $a3 = "STRING"
    condition:
        1 of them
}