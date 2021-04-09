# base64_cli_python
base64_cli_python is a cli tool that easily decodes base64 encoded multiple times.
## set up
```
$ pip install git+https://github.com/haru0017/multiple-base64
```
## encode
```
$ mbase64 -e python
encode: cH10aG9u
```
You can also specify the number of encodings.
```
$ mbase64 -e python -t 10
encode: Vm0wd2VHUXhTWGhXV0doVFYwZDRWVll3WkRSV2JGbDNXa1pPVlUxV2NIcFhhMk0xVmpGS2RHVkdXbFpOYWtFeFZtMTRZV015U2tWVWJHUk9ZbTFvYjFac1ZtRldNVnBXVFZWV2FHVnFRVGs9
```
## decode
You can decode text that you do not know how many times it has been encoded in one shot.
```
$ mbase64 -d Vm0wd2VHUXhTWGhXV0doVFYwZDRWVll3WkRSV2JGbDNXa1pPVlUxV2NIcFhhMk0xVmpGS2RHVkdXbFpOYWtFeFZtMTRZV015U2tWVWJHUk9ZbTFvYjFac1ZtRldNVnBXVFZWV2FHVnFRVGs9
decode: python
