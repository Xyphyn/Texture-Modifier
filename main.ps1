$a = [reflection.assembly]::LoadWithPartialName("System.Drawing")

Get-ChildItem -Recurse -Filter *.png |
ForEach-Object {


$path_loc = $_.FullName
$bytes = [System.IO.File]::ReadAllBytes($path_loc)
$ms = new-object System.IO.MemoryStream(,$Bytes)
$OldBitmap = [system.drawing.Image]::FromStream($ms)

$path_loc

foreach($y in (0..($OldBitmap.Height-1))) {
foreach($x in (0..($OldBitmap.Width-1))) {
$bit = $OldBitmap.GetPixel($x,$y)
$col = $bit.GetBrightness() * 255
$slateBlue = [System.Drawing.Color]::FromArgb($bit.A,$col, $col, $col)
try {$oi = $OldBitmap.SetPixel($x,$y,$slateBlue)
} catch {
    #do literally nothing
}
}}
$OldBitmap.Save(((Get-Location).path + "\testin.png"))
$OldBitmap.Dispose()
Remove-Item ($path_loc)
Move-Item (((Get-Location).path + "\testin.png")) ($path_loc)
}