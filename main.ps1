$a = [reflection.assembly]::LoadWithPartialName("System.Drawing")
$OldBitmap = new-object System.Drawing.Bitmap "test.png"
$g=[System.Drawing.Graphics]::FromImage($OldBitmap)
foreach($y in (0..($OldBitmap.Height-1))) {
foreach($x in (0..($OldBitmap.Width-1))) {
$bit = $OldBitmap.GetPixel($x,$y)
$col = $bit.GetBrightness() * 255
$slateBlue = [System.Drawing.Color]::FromArgb($bit.A,$col, $col, $col)
$OldBitmap.SetPixel($x,$y,$slateBlue)
}}
$OldBitmap.Save(((Get-Location).path + "\test2.png"))