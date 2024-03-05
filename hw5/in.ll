define i64 @jitentry(i64 %arg0) {
start:
  %big = icmp sgt i64 %arg0, 5
  br i1 %big, label %bigger, label %done

bigger:
  %scaled = mul i64 %arg0, 10
  br label %done

done:
  %x = add i64 %scaled,0
  ret i64 %x
}
