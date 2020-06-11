library(DSS)
args = commandArgs(trailingOnly=TRUE)

###############################################################

#Cov <- as.matrix(read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region_Cov.txt",header=T,sep="\t",check.names=FALSE))
#M <- as.matrix(read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region_M.txt",header=T,sep="\t",check.names=FALSE))
#Loci <- read.table("../5_rerun_DSS_approach/filtered_matrix/HumanChimpMacaq_species_region.info.txt",header=T,sep="\t",check.names=FALSE)
#bs.combine.filtered <- BSseq(chr = Loci$chr, pos = Loci$start , M = M, Cov = Cov, sampleNames = colnames(M))

bs.combine.filtered <- readRDS(args[1])
###do not change#############################################################
macaq.ind <- sampleNames(bs.combine.filtered)[grep("YN",sampleNames(bs.combine.filtered))]
human.ind <-sampleNames(bs.combine.filtered)[grep("Control",sampleNames(bs.combine.filtered))]
chimp.ind <- sampleNames(bs.combine.filtered)[!(sampleNames(bs.combine.filtered) %in% c(human.ind,macaq.ind))]
covariates_R <- read.table("../../bsseq/matrix/covariates_all.txt",header=T)
row.names(covariates_R) <- covariates_R$GT_ID

####################################################################

#bs.species.CH <- bs.combine.filtered[,c(chimp.ind,human.ind)]
#bs.species.CM <- bs.combine.filtered[,c(chimp.ind,macaq.ind)]
#bs.species.HM <- bs.combine.filtered[,c(human.ind,macaq.ind)]

###########

covariates_R_order <- data.frame(covariates_R[c(sampleNames(bs.combine.filtered)),])
#covariates_R_order$Age_Class <- as.factor(covariates_R_order$Age_Class)
covariates_R_order$NHP <-c(rep("H",10),rep("N",20))
covariates_R_order <- droplevels(covariates_R_order)
pData(bs.combine.filtered)$CellType <- covariates_R_order$CellType
pData(bs.combine.filtered)$Species <- covariates_R_order$Species
pData(bs.combine.filtered)$Sex <- covariates_R_order$Sex
pData(bs.combine.filtered)$Age_Class <- covariates_R_order$Age_Class
pData(bs.combine.filtered)$Conversion_rates <- covariates_R_order$Conversion_rates
pData(bs.combine.filtered)$NHP <- covariates_R_order$NHP
pData(bs.combine.filtered)<- droplevels(pData(bs.combine.filtered))
pData(bs.combine.filtered)$Species <- factor(pData(bs.combine.filtered)$Species, levels = c("Human", "Chimp", "Macaque"))

############

#model.matrix(~Species+CellType+Sex+Age_Class+Conversion_rates+Species:CellType,pData(bs.PR.olig))
#SpeciesHuman SpeciesMacaque CellTypeOlig SpeciesHuman:CellTypeOlig


###############

DMLfit = DMLfit.multiFactor(bs.combine.filtered,pData(bs.combine.filtered), ~Species+Sex+Age_Class+Conversion_rates+NHP:Age_Class)
#DMLtest = DMLtest.multiFactor(DMLfit, term="Age_Class:NHP")
DMLtest = DMLtest.multiFactor(DMLfit, term="Age_Class")

fdr_max <- DMLtest[DMLtest$fdrs<0.05,][which.max(DMLtest[DMLtest$fdrs<0.05,]$pvals),]
ix=sort.int(DMLtest[,"pvals"], index.return=TRUE,na.last=TRUE)$ix
write.table(DMLtest[ix,],file=paste0(args[2],"_DML_Species_Age_interaction_fdrs.txt"),sep="\t",row.names=F,quote=F)

DMRtest <- callDMR(DMLtest, p.threshold=0.01,minCG=3)
#DMRtest_filtered <- DMRtest[(abs(DMRtest$areaStat) / DMRtest$nCG) > abs(fdr_max$stat),]
write.table(DMRtest,file=paste0(args[2],"_DMR_Species_Age_interaction_fdrs.txt"),sep="\t",row.names=F,quote=F)





#write.table(DMLtest,file=paste0(args[2],"_Species.txt"),sep="\t",row.names=F,quote=F)

#DMLfit = DMLfit.multiFactor(bs.species.CH,pData(bs.species.CH), ~Species+Sex+Age_Class+Conversion_rates)
#DMLtest = DMLtest.multiFactor(DMLfit, coef="SpeciesHuman")
#write.table(DMLtest,file=paste0(args[2],"_Species_HvsC.txt"),sep="\t",row.names=F,quote=F)

#DMLfit = DMLfit.multiFactor(bs.species.CM,pData(bs.species.CM), ~Species+Sex+Age_Class+Conversion_rates)
#DMLtest = DMLtest.multiFactor(DMLfit, coef="SpeciesMacaque")
#write.table(DMLtest,file=paste0(args[2],"_Species_MvsC.txt"),sep="\t",row.names=F,quote=F)

#DMLfit = DMLfit.multiFactor(bs.species.HM,pData(bs.species.HM), ~Species+Sex+Age_Class+Conversion_rates)
#DMLtest = DMLtest.multiFactor(DMLfit, coef="SpeciesMacaque")
#write.table(DMLtest,file=paste0(args[2],"_Species_MvsH.txt"),sep="\t",row.names=F,quote=F)

##############






