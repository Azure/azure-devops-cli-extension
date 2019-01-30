# Authoring Live Tests

Make sure your machine python SDK cache is clear

It is located at `%userprofile%\.vsts\python-sdk\cache\`

While running the test localy for first time make sure that the cassest (in the recording folder) gets the resource call as well

Before commiting the code make sure to randomize the PAT token

## Known issues

In case you run into error where the size of response is too large to be recorded
you can use this decorator on top of the test case
@AllowLargeResponse(size_kb=3072)

## Points to remember

- Actual Test Setup/ Environment should be kept intact (i.e. maintained) so that if someone new wants to re-run and
  re-record the test case (with a proper PAT token) then they should be able to
