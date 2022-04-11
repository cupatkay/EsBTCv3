# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'ZnJvbSByZSBpbXBvcnQgUw0KaW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgc3lzDQppbXBvcnQgc2lnbmFsDQpmcm9tIGx4bWwgaW1wb3J0IGh0bWwNCmltcG9ydCBvcw0KaW1wb3J0IHRpbWUNCmltcG9ydCBjb2xvcmFtYQ0KaW1wb3J0IGlvDQppbXBvcnQganNvbg0KZnJvbSByYW5kb20gaW1wb3J0ICoNCmltcG9ydCByYW5kb20NCmltcG9ydCBwbGF0Zm9ybQ0KaW1wb3J0IHdlYmJyb3dzZXINCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUsIEJhY2ssIFN0eWxlLCBpbml0DQpmcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cA0KZnJvbSBjZmcgaW1wb3J0IGNvb2tpZSwgdWlkLCB1c2VyX2FnZW50LCBoYXNoX2luaQ0KDQoNCmRlZiBkZWZfaGFuZGxlcihzaWcsIGZyYW1lKToNCiAgICBzeXMuZXhpdCgwKQ0Kc2lnbmFsLnNpZ25hbChzaWduYWwuU0lHSU5ULCBkZWZfaGFuZGxlcikNCg0KZGVmIG9wZW5feW91dHViZSgpOg0KICAgIGlmIHBsYXRmb3JtLnN5c3RlbSgpID09ICJMaW51eCI6DQogICAgICAgIG9zLnN5c3RlbSgidGVybXV4LW9wZW4gaHR0cHM6Ly93d3cueW91dHViZS5jb20vY2hhbm5lbC9VQ29ZVzRrUnc0MkxHYm1UWVFQZzB6UUEiKQ0KICAgIGVsc2U6DQogICAgICAgIHdlYmJyb3dzZXIub3BlbignaHR0cHM6Ly93d3cueW91dHViZS5jb20vY2hhbm5lbC9VQ29ZVzRrUnc0MkxHYm1UWVFQZzB6UUEnKQ0KICAgIHRpbWUuc2xlZXAoMSkNCm9wZW5feW91dHViZSgpDQoNCg0KZGVmIGxpbXBpYXIoKToNCiAgICB0aW1lLnNsZWVwKDIpDQogICAgaWYgcGxhdGZvcm0uc3lzdGVtKCkgPT0gIldpbmRvd3MiOg0KICAgICAgICBvcy5zeXN0ZW0oJ2NscycpDQogICAgZWxpZiBwbGF0Zm9ybS5zeXN0ZW0oKSA9PSAiTGludXgiOg0KICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykNCmxpbXBpYXIoKQ0KDQoNCmRlZiBjb250YWRvcihzZWNvbmQpOg0KCXdoaWxlIHNlY29uZDoNCgkJbWlucywgc2VjcyA9IGRpdm1vZChzZWNvbmQsIDYwKQ0KCQl0aW1lciA9IGxyb2pvKyLilrYgIitsY3lhbisiRXNwZXJlICIrbGFtYXJpbGxvICsgXA0KCQkgICAgIih7OjAyZH06ezowMmR9KSIuZm9ybWF0KG1pbnMsIHNlY3MpK3Jlc3Rjb2xvcg0KCQlwcmludCh0aW1lciwgZW5kPSJcciIpDQoJCXRpbWUuc2xlZXAoMSkNCgkJc2Vjb25kIC09IDENCg0KDQpkZWYgbGVudG8odGV4dG8pOg0KICAgIHRyeToNCiAgICAgICAgZm9yIGxldHJhIGluIHRleHRvOg0KICAgICAgICAgICAgcHJpbnQobGV0cmEsIGVuZD0nJywgZmx1c2g9VHJ1ZSkNCiAgICAgICAgICAgIHRpbWUuc2xlZXAoMC4wMjUpDQogICAgZmluYWxseToNCiAgICAgICAgcGFzcw0KDQoNCiMgdmFyaWFibGVzIGRlIGNvbG9yDQphenVsID0gRm9yZS5CTFVFDQpuZWdybyA9IEZvcmUuQkxBQ0sNCmN5YW4gPSBGb3JlLkNZQU4NCnZlcmRlID0gRm9yZS5HUkVFTg0KbGF6dWwgPSBGb3JlLkxJR0hUQkxVRV9FWA0KbG5lZ3JvID0gRm9yZS5MSUdIVEJMQUNLX0VYDQpsY3lhbiA9IEZvcmUuTElHSFRDWUFOX0VYDQpsbWFnZW50YSA9IEZvcmUuTElHSFRNQUdFTlRBX0VYDQpsdmVyZGUgPSBGb3JlLkxJR0hUR1JFRU5fRVgNCmxhbWFyaWxsbyA9IEZvcmUuTElHSFRZRUxMT1dfRVgNCmxyb2pvID0gRm9yZS5MSUdIVFJFRF9FWA0KbGJsYW5jbyA9IEZvcmUuTElHSFRXSElURV9FWA0KZmxhenVsID0gQmFjay5MSUdIVEJMVUVfRVgNCmZsY3lhbiA9IEJhY2suTElHSFRDWUFOX0VYDQpmbHJvam8gPSBCYWNrLkxJR0hUUkVEX0VYDQpmbHZlcmRlID0gQmFjay5MSUdIVEdSRUVOX0VYDQpmbGFtYXJpbGxvID0gQmFjay5MSUdIVFlFTExPV19FWA0KZmxibGFuY28gPSBCYWNrLkxJR0hUV0hJVEVfRVgNCnJlc3Rjb2xvciA9IEZvcmUuUkVTRVQNCnJlc2V0Zm9uZG8gPSBCYWNrLlJFU0VUDQpicmlsbG8gPSBTdHlsZS5CUklHSFQNCmhvcmEgPSB0aW1lLnN0cmZ0aW1lKCIlSDolTTolUyIpDQoNC'
love = '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'
god = 'B2M3tyZXN0Y29sb3J9e3Jlc2V0Zm9uZG99DQrimpzvuI97YnJpbGxvfXtsY3lhbn0gIENyZWFkbyBwb3I6IHtsYW1hcmlsbG99VFVESU5FUk9XRUJ7cmVzdGNvbG9yfQ0K4pqc77iPe2JyaWxsb317bGN5YW59ICBDYW5hbCBZb3V0dWJlOiB7bGFtYXJpbGxvfXR1ZGluZXJvd2Vie3Jlc3Rjb2xvcn0NCuKanO+4j3ticmlsbG99e2xjeWFufSAgdGVsZWdyYW0gR3J1cG86IHtsYW1hcmlsbG99VHVEaW5lcm9XZWJfR3JvdXB7cmVzdGNvbG9yfQ0KIiIiDQplc3RhZG8oKQ0KbGVudG8oQmFubmVyKQ0KDQpsaW5lYSA9ICItLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuIg0KbGVudG8obGluZWEpDQoNCmhlYWRlcnMgPSB7DQogICAgIkhvc3QiOiAiZXMuYnRjbmV3ei5jb20iLA0KICAgICJ1c2VyLWFnZW50IjogIk1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA4LjEuMDsgUmVkbWkgNSBCdWlsZC9PUE0xLjE3MTAxOS4wMjY7IHd2KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBWZXJzaW9uLzQuMCBDaHJvbWUvOTguMC40NzU4LjEwMSBNb2JpbGUgU2FmYXJpLzUzNy4zNiIsDQp9DQojIGluaWNpYW1vcyBzZWNjaW9uIGNvbiBlbCBsaW5rIG1pbmVyIA0KDQpsb2dpbiA9IGYiaHR0cHM6Ly9lcy5idGNuZXd6LmNvbS91c2VyL21pbmVyLzI/dWlkPXt1SUR9Ig0KcmVzcHVlc3RhID0gc2Vzc2lvbi5nZXQobG9naW4sIGhlYWRlcnM9aGVhZGVycykNCmxhcmF2ZWwgPSByZXNwdWVzdGEuY29va2llcw0KbGFyYXZlbF9kaWN0ID0gbGFyYXZlbC5nZXRfZGljdCgpDQpjb29rID0gbGFyYXZlbF9kaWN0WydsYXJhdmVsX3Nlc3Npb24nXQ0KIyBwcmludChjb29rKQ0KDQpoZWFkZXJzMSA9IHsNCiAgICAiSG9zdCI6ICJlcy5idGNuZXd6LmNvbSIsDQogICAgInVzZXItYWdlbnQiOiAiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMS4wOyBSZWRtaSA1IEJ1aWxkL09QTTEuMTcxMDE5LjAyNjsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vNC4wIENocm9tZS85OC4wLjQ3NTguMTAxIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwNCiAgICAiY29va2llIjogZiJsYXJhdmVsX3Nlc3Npb249e2Nvb2t9IiwNCn0NCmhlYWRlcnMyID0gew0KICAgICJIb3N0IjogImVzLmJ0Y25ld3ouY29tIiwNCiAgICAiYWNjZXB0LWxhbmd1YWdlIjogImVzLVBFLGVzO3E9MC45LGVuLVVTO3E9MC44LGVuO3E9MC43IiwNCiAgICAiY29va2llIjogY29va2llLA0KICAgICJvcmlnaW4iOiAiaHR0cHM6Ly9lcy5idGNuZXd6LmNvbSIsDQogICAgInJlZmVyZXIiOiAiaHR0cHM6Ly9lcy5idGNuZXd6LmNvbS91c2VyL21pbmVyLzIiLA0KICAgICJzZWMtZmV0Y2gtZGVzdCI6ICJlbXB0eSIsDQogICAgInNlYy1mZXRjaC1tb2RlIjogImNvcnMiLA0KICAgICJzZWMtZmV0Y2gtc2l0ZSI6ICJzYW1lLW9yaWdpbiIsDQogICAgInVzZXItYWdlbnQiOiB1c2VyX2FnZW50LA0KICAgICJ4LXJlcXVlc3RlZC13aXRoIjogIlhNTEh0dHBSZXF1ZXN0IiwNCn0NCg0KbG9naW4gPSBmImh0dHBzOi8vZXMuYnRjbmV3ei5jb20vdXNlci9taW5lci8yP3VpZD17dUlEfSINCnJlc3B1ZXN0YSA9IHNlc3Npb24uZ2V0KGxvZ2luLCBoZWFkZXJzPWhlYWRlcnMxKQ0KcGFyc2VyID0gaHRtbC5mcm9tc3RyaW5nKHJlc3B1ZXN0YS50ZXh0KQ0KdXNlciA9IHBhcnNlci54cGF0aCgiLy9oNFtjb250YWlucyhAY2xhc3MsICdwYW5lbC10aXRsZScpXS90ZXh0KCkiKQ0KZm9yIHVzIGluIHVzZXI6DQogICAgcHJpbnQoZmxibGFuY28rYnJpbGxvK2xuZWdybyt1cytyZXN0Y29sb3IrcmVzZXRmb25kbysnXG4nKQ0KIyBwcmludChyZXNwdWVzdGEuY29udGVudCkNCg0KaW5pID0gaGFzaF9pbmkNCndoaWxlIFRydWU6DQogICAgdHJ5Og0KICAgICAgICByYW5kID0gcmFuZG9tLnJ'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
