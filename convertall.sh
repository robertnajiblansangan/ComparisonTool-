#!/usr/bin/env python

convert_psa2() {
mkdir -p ./PSA2-out

for line in $(find ./PSA2 -type f -name '*'); do
    ##service=`xmlstarlet sel -t -v '//ns0:Field-Service[1]/text()' -n ${line}`
    ##vessel=`xmlstarlet sel -t -m '//ns0:Field-Vessel[1]' -v . -n ${line}`
    ##voy=`xmlstarlet sel -t -m '//ns0:Field-Vessel[1]' -v . -n ${line}`
    
    ##echo ${service}-${vessel}-${voy}
    echo ${line}
    bname=`basename ${line}`

    ./xml2json.py --strip_newlines --pretty \
      --strip_namespace  ${line} > ./PSA2-out/${bname}.t0.json
    jq -S . ./PSA2-out/${bname}.t0.json \
      | jq  '. as $raw | ."Message-PSACOPRAR"."GroupRecord-Container_Group"|= try sort_by(."Record-ContainerRec"."Field-CntNo"."#text") catch $raw ' \
      | jq -M 'del(.. | ."@DataType" ?)' \
      | jq -M 'del(.. | ."@{http://www.w3.org/2001/XMLSchema-instance}nil" ?)' \
      | jq -M 'del(.. | ."#tail" ?)' \
      | jq '.' > ./PSA2-out/${bname}.json
    rm -rf ./PSA2-out/${bname}.t*

#   echo ${ele}
done
}

convert_psa() {
mkdir -p ./PSA-out

for line in $(find ./PSA -type f -name '*'); do
    ##service=`xmlstarlet sel -t -v '//ns0:Field-Service[1]/text()' -n ${line}`
    ##vessel=`xmlstarlet sel -t -m '//ns0:Field-Vessel[1]' -v . -n ${line}`
    ##voy=`xmlstarlet sel -t -m '//ns0:Field-Vessel[1]' -v . -n ${line}`
    
    ##echo ${service}-${vessel}-${voy}
    echo ${line}
    bname=`basename ${line}`

    ./xml2json.py --strip_newlines --pretty \
      --strip_namespace  ${line} > ./PSA-out/${bname}.t0.json
    jq -S . ./PSA-out/${bname}.t0.json \
      | jq  '. as $raw | ."Message-PSACOPRAR"."GroupRecord-Container_Group"|= try sort_by(."Record-ContainerRec"."Field-CntNo"."#text") catch $raw ' \
      | jq -M 'del(.. | ."@DataType" ?)' \
      | jq -M 'del(.. | ."#tail" ?)' \
      | jq '.' > ./PSA-out/${bname}.json
    rm -rf ./PSA-out/${bname}.t*
  
    ## dir=`xmlstarlet sel -t -m '//ns0:Field-Vessel' -v . -n ${line}`
#   echo ${ele}
done
}

convert_psa2;
convert_psa;