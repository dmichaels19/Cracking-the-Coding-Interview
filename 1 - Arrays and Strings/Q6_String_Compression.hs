
stringCompression :: String -> String
stringCompression "" = ""
stringCompression str = if length compressed < length str then compressed else str
  where compressed = compressString restStr "" firstChar count
        firstChar = head str
        restStr = tail str
        count = 1

compressString :: String -> String -> Char -> Int -> String
compressString "" compressed currChar count           = compressed ++ (currChar : show count)
compressString (x:uncompr) compressed currChar count
  | currChar == x = compressString uncompr compressed currChar (count + 1)
  | otherwise     = compressString uncompr compressed' x 1
    where compressed' = compressed ++ (currChar : show count)


compressString2 :: String -> String
compressString2 str = foldr printer "" $ foldr compressor [] str
  where compressor :: Char -> [(Char, Int)]  -> [(Char, Int)]
        compressor next [] = [(next, 1)]
        compressor next all@((last, count) : rest) | last == next = (last, count + 1) : rest
                                                   | otherwise    = (next, 1) : all
        printer (chr, count) str = chr : show count ++ str
