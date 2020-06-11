args = commandArgs(trailingOnly=TRUE)
require(data.table)
DT<- fread(args[1])
M1<-colSums(DT<=0.2)
M2<-colSums(DT>0.2 & DT <=0.4)
M3<-colSums(DT>0.4 & DT <=0.6)
M4<-colSums(DT>0.6 & DT <=0.8)
M5<-colSums(DT>0.8 & DT <=1)
count_meth <- t(data.frame(M1,M2,M3,M4,M5))
write.table(count_meth,file=args[2],quote=F,sep='\t')
