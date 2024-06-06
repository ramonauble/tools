---------------------------------------------
tools & miscellanea
by ramona a -w-              ←-___←↑→__-→
7-25-20                     ←-///π\//π \\-→
><>|^*^|<><                 ←-\\π↓|↑|↓π//-→
_______                      ←-\\π+r+π//-→
--___--                       ←-\\π+π//-→
  |||___-π-___...              ←-\\↑//-→
  |||---|||---|||               ←-\π/-→
 / π \       / π \               ←-|-→
 \___/       \___/                ←↓→
---------------------------------------------
                Description
---------------------------------------------

this is a repository for different devlopment tools
and spurious one-offs which don't warrant a repo all their own

currently contains:
---------------------------------------------
  • wv_gen
  ---------------------------------------
    • language: python
    • purpose:  to generate an ordered table comprised of a list of samples
      representing a single cycle of a waveform
      as determined by some arbitrary function
      (currently a nonscaled, nonshifted linear polynomial)
      (y = x) - for linear envelope curve
      
  • freq_gen
  ---------------------------------------
    • language: python
    • purpose:  to generate an ordered table comprised of a list of frequencies
      expressed as integers, scaled exponentially as per the 12TET scale
  
  • wav_test
  ---------------------------------------
    • language: python
    • purpose: test generating a valid wav file header (for arbitrary wav file generation)

  • textToASCII
  ---------------------------------------
    • language: python
    • purpose: converts arbitray string (no spaces) to binary/decimal/octal/symbolic octal ASCII format

  • posFinder
  ---------------------------------------
    • language: python
    • purpose: spaces n objects on axis x/y/z by +/- amount Amm
      • optional offset allows starting position to be shifted along the selected axis
      • optional grouping adds additional space of size Bmm every m objects
  ---------------------------------------

      
     

