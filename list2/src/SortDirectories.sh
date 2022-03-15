$path = $args[0]
$nfiles_to_show = $args[1]
$files = (Get-ChildItem -path $path -Recurse | Select-Object Name, Size -First $nfiles_to_show | Sort-Object -Property Size -Descending)
$result = @()

echo $files