-- TODO: DOES NOT COMPILE

data Edited = Used | Unused deriving (Eq)


oneAway :: Eq a => [a] -> [a] -> Bool
oneAway xs ys
  | xLen == yLen    = tryReplace xs ys Unused
  | xLen -1 == yLen = needDelete xs ys Unused
  | xLen == yLen -1 = needDelete ys xs Unused
  | otherwise       = False
  where xLen = length xs
        yLen = length ys
        tryReplace as bs Used      = as == bs
        tryReplace (a:as) (b:bs) _ = let used = if (a == b) then Unused else Used
                                      in tryReplace as bs used
        tryReplace [] [] _         = True

needDelete as bs Used               = as == bs
needDelete (a:as) (b:bs) Unused     = if (a == b) then needDelete as bs Unused
                                                  else needDelete as (b:bs) Used
needDelete _ _ _                    = True
