{- Implement an algorithm to determine if a string has all unique characters.
   What if you can't use additional data structures?
-}

import Data.List (sort)

isUnique :: Ord a => [a] -> Bool
isUnique = isUnique' . sort
  where isUnique' (x:y:xs) = (x /= y) && isUnique' (y:xs)
        isUnique' _        = True
