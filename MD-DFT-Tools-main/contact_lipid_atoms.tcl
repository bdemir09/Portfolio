set mol [molinfo top]
set sel [atomselect $mol {(resname DPPE and name C213) and within 5.0 of (nucleic or resname 3CHL)}]
set frames [molinfo $mol get numframes]
set fp [ open "DPPE_nameC213_within5oforigami.dat" w ]
for {set i 0} {$i < $frames} {incr i} {
    $sel frame $i
    $sel update
    set n [$sel num]
    puts $fp "$i $n"
}
$sel delete
close $fp

exit