set outfile [open rmsf_n.dat w];                                             
set sel [atomselect top "nucleic and backbone and name C5' "]
puts $outfile "[measure rmsf $sel first 1 last -1 step 100]"
close $outfile