import Development.Shake
import Development.Shake.Command
import Development.Shake.FilePath
import Development.Shake.Util

main :: IO ()
main = shakeArgs shakeOptions{shakeFiles="_build"} $ do

    "*.html" %> \out -> do
        let org = out -<.> "org"
        let template = "default.revealjs"
        need [org, template]
        cmd_ "pandoc --standalone -t revealjs" ["--template="++template] "-o" [out] [org]
