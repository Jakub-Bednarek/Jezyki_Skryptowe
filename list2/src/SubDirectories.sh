$path = $args[0]
$count = (Get-ChildItem -Path $path -Directory -Recurse).Count 

'Liczba podfolderow w folderze {0}: {1}' -f $path, $count