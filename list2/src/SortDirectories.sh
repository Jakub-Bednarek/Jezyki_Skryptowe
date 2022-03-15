$pattern = $args[0]
$path = $args[1]
$nfiles_to_show = $args[2]
$files = (Get-ChildItem -path $path -Recurse | Sort-Object -Property Size -Descending) | Where-Object { $_.name -Match $pattern } | Select-Object Name, Size -First $nfiles_to_show 
$result = @()

echo $files