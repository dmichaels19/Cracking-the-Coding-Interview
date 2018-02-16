import System.Random

main = do
  g <- newStdGen
  let out = getRandomRange g 1 10
  let out1 = getRandomRange g 1 10
  let out2 = getRandomRange g 1 10
  print $ out

shuffle :: StdGen -> [Int] -> [Int]
shuffle _ []      = []
shuffle _ (x: []) = [x]
shuffle g xs      = shuffle' g 0 xs
  where shuffle' gen i xs
        | i < length xs = shuffle' gen' (i + 1) $ swap xs i j
        where random = getRandomRange g i (length xs - 1)
              gen'   = snd random
              j      = fst random
        | otherwise     = xs

swap :: [Int] -> Int -> Int -> [Int]
swap xs i j = beginning ++ [xs !! j] ++ middle ++ [xs !! i] ++ rest
  where beginning = take (i-1) xs
        middle = take (i - j - 1) $ drop i xs
        rest = drop j xs

getRandomRange :: StdGen -> Int -> Int -> Int
getRandomRange g low high = fst $ randomR (low, high) g
