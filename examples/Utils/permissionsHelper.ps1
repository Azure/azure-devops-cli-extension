function displayPermissions{
    param([object]$permissionsResponse)
    
    foreach($acl in $permissionsResponse)
    {
            $ace = $acl.acesDictionary
            $ace_key = $ace | Get-Member -MemberType NoteProperty | Select -ExpandProperty Name
            $ace_value= $ace.$ace_key
            $permissionsList =   $($ace_value.resolvedPermissions)
            foreach($perm in $permissionsList)
            {
                Write-Host "$($perm.displayName) [$($perm.bit)] , $($perm.effectivePermission)"
            }
    }
}
