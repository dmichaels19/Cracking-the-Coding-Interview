import Data.Char (toLower)
import Data.List (sort)

isPermutation :: [Char] -> Bool
isPermutation = allPairsButOne . sort . stringToLower . removeWhitespace

allPairsButOne xs = allPairsButOne' xs False
  where allPairsButOne' :: String -> Bool -> Bool
        allPairsButOne' (x:y:rest) foundUnique = case foundUnique of
                                                   True   ->    (x==y) &&   allPairsButOne' rest True
                                                   False  -> if (x==y) then allPairsButOne' rest False
                                                                       else allPairsButOne' (y : rest) True
        allPairsButOne' [] _ = True
        allPairsButOne' (x) False = True
        allPairsButOne' (x) True = False


stringToLower = map toLower

removeWhitespace = filter (\x -> x /= ' ')


-- isPermutation = allPairsButOne . sort . stringToLower . removeWhitespace
