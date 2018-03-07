{-
    Write a method to replace all spaces in a string with '%20'.
-}

urlify (x:xs)
  | x == ' '   = "%20" ++ urlify xs
  | otherwise  = x : urlify xs
urlify []      = []
