args = commandArgs(trailingOnly=TRUE)
require(data.table)

DT<- fread(args[1],sep="\t")
DT$Human_meth_diff <- DT$Human_ND_meth - DT$Human_OD_meth
DT$Chimp_meth_diff <- DT$Chimp_ND_meth - DT$Chimp_OD_meth
DT$Macaque_meth_diff <- DT$Macaque_ND_meth - DT$Macaque_OD_meth
DT <- DT[,c("Human_meth_diff","Chimp_meth_diff","Macaque_meth_diff")]
M1<-colSums(DT>= -1 & DT< -0.5)
M2<-colSums(DT>= -0.5 & DT< -0.2)
M3<-colSums(DT>= -0.2 & DT< 0)
M4<-colSums(DT>0 & DT <=0.2)
M5<-colSums(DT>0.2 & DT <=0.5)
M6<-colSums(DT>0.5 & DT <=1)
count_meth <- t(data.frame(M1,M2,M3,M4,M5,M6))
write.table(count_meth,file=args[2],quote=F,sep='\t')

