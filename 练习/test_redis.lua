
key = "/api/sql/rest/query/yyXDAAwgIMTjZxFXLLak?12123"

function split( s, c )
        for item in string.gmatch( s, "(.-)"..c) do
                keys = item
                if not keys then
                        ngx.say("failed to get key: ", err)
                        end
                end
end
split(key , "?" )

print(keys)
key1= "/api/sql/rest/query/yyXDAAwgIMTjZxFXLLak?12123"



function trim(s)
        return (string.gsub(s, "^/*(.-)%s*$", "%1"))end

key1= "/api/sql/rest/query/yyXDAAwgIMTjZxFXLLak"
print(trim(key1))
