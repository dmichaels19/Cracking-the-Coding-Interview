{-
  Given two strings, write a method to decide if one is a permutation of the other.
-}

import Data.List (sort)

checkPermutation :: Ord a => [a] -> [a] -> Bool
checkPermutation a b = sort a == sort b

checkPermutationBetter a b
  | length a /= length b = False
  | otherwise            = checkPermutation a b
