# base64_cli_python
base64_cli_python is a cli tool that easily decodes base64 encoded multiple times.
## set up
```
$ pip install git+https://github.com/haru0017/multiple-base64
```
## encode
```
$ base -e twitter
encode: dHdpdHRlcg==
```
You can also specify the number of encodings.
```
$ base -e twitter -t 10
encode: Vm0wd2VHUXhUWGROVldSWVYwZDRWVll3WkRSV1JsbDNXa1JTVjJKSGVGWlZNakExVmpBeFdHVkdXbFpOYmtKVVZtcEJlRmRIVmtsalJuQlhWakF3ZUZkV1pEUlpWMUpIVm01R1UySklRbTlaV0hCWFpWWmFjMVp0UmxkTlZuQlhWRlpXVjJGSFZuRlJWR3M5
```
## decode
You can decode text that you do not know how many times it has been encoded in one shot.
```
$ base -d Vm0wd2VHUXhUWGROVldSWVYwZDRWVll3WkRSV1JsbDNXa1JTVjJKSGVGWlZNakExVmpBeFdHVkdXbFpOYmtKVVZtcEJlRmRIVmtsalJuQlhWakF3ZUZkV1pEUlpWMUpIVm01R1UySklRbTlaV0hCWFpWWmFjMVp0UmxkTlZuQlhWRlpXVjJGSFZuRlJWR3M5
decode: twitter
