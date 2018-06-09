PROTO_SRC=../../../Shared/Communication/Messages/
MESSAGE_DST=./Messages

for file in $PROTO_SRC/*.proto; do

  echo "Generating python messaging for file " $file " in " $PROTO_SRC

  protoc -I=$PROTO_SRC --python_out=$MESSAGE_DST $file
done
