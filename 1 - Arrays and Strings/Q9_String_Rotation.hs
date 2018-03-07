import Data.List (isInfixOf)

stringRotation str1 str2 = len1 == len2 && str1 `isInfixOf` (str2 ++ str2)
  where len1 = length str1
        len2 = length str2
