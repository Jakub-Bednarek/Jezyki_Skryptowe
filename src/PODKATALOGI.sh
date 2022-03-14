$path = $args[0]
$count = (Get-ChildItem -Recurse -Directory | Measure-Object).Count

'Liczba folderow w podfolderze {0}: {1}' -f $path, $count