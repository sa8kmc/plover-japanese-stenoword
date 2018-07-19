# Plover Japanese (StenoWord)

The Japanese StenoWord stenography system for Plover.

## Activating StenoWord

After installing this plugin, you need to turn it on in Plover:

1. In Plover's configuration, go to the ``Systems`` tab, and change the active system to ``Japanese StenoWord``.
2. You can use either a Qwerty keyboard or a keyboard speaking TxBolt (e.g. SOFT/HRUF Splitography) to use this theory.

## Layout

### TxBolt (Protocol for English Steno)

```
#  #  #  #  #  #  #  #  #  #
P  T  H  K  S  U  A  O  I  E
P  T  H  K  S  U  A  O  I  E
      L  M     N  R
```
which originally look like:
```
#  #  #  #  #  #  #  #  #  #
S- T- P- H- * -F -P -L -T -D
S- K- W- R- * -R -B -G -S -Z
      A- O-   -E -U
```

#### Notes 

- 2 rows are exactly same. (TODO: Utilize one row for other usage)
- Home position for right hand is shifted to the right. First finger is on `K` and `A`.
- `#` is used for Undo.
- S is also on the right side

### Keyboard
```
 #  #  #  #  #  #  #  #  #  #
  P  T  H  K  S  U  A  O  I  E
   -  -  L  M  -  N  R  -  -  
            arpeggiate             
```
which originally look like
```
 q  w  e  r  t  y  u  i  o  p 
  a  s  d  f  g  h  j  k  l  ;
   z  x  c  v  b  n  m  ,  .  
            space             
```


## Command dictionary

There is no special entries like space or new line yet.

- `S#`: Set space as empty string. In order not to output spaces between strokes.
