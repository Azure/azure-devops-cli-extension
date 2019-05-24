function set_policies(
    [String]$org,
    [String]$projectName,
    [String]$repoId,
    [String]$branch,
    [string[]]$requiredApprovers,
    [string[]]$optionalApprovers
)
{
    if($requiredApprovers)
    {
        $reviewersRequired = ''
        foreach($reviewer in $requiredApprovers)
        {
            $reviewersRequired= $reviewersRequired + $reviewer +';'
        }
        
        $reviewersRequired = $reviewersRequired.Substring(0,$reviewersRequired.Length-1)
        $reviewerPolicy = az repos policy required-reviewer create --org $org -p $projectName --branch $branch --repository-id $repoId --is-blocking true --is-enabled true --message 'Required reviewers policy added' --required-reviewer-ids $reviewersRequired -o json | ConvertFrom-Json
    }    
    # set optional reviewers
    if($optionalApprovers)
    {
        $reviewersOptional = ''
        foreach($reviewer in $optionalApprovers)
        {
            $reviewersOptional= $reviewersOptional + $reviewer +';'
        }
        $reviewersOptional = $reviewersOptional.Substring(0,$reviewersOptional.Length-1)
        $reviewerPolicy = az repos policy required-reviewer create --org $org -p $projectName --branch $branch --repository-id $repoId --is-blocking false --is-enabled true --message 'Optional reviewers policy added' --required-reviewer-ids $reviewersOptional -o json | ConvertFrom-Json
    }
}
