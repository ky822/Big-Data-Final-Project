library(ggplot2)
library(ggmap)
library(maps)
library(mapproj)
setwd('/Users/keye/Documents/= =/Spring 2015/Big\ Data')
setwd('/Users/keye/Documents/= =/Spring 2015/Big\ Data/R_map')


label_data = read.table("label_data",header = FALSE,sep='\t')

colnames(label_data)<-c('key','tip','lon','lat','boro')

l_1 =  read.table("Jan_1",header = FALSE,sep='\t')
l_2 =  read.table("Jan_2",header = FALSE,sep='\t')
l_3 =  read.table("Jan_3",header = FALSE,sep='\t')
l_4 =  read.table("Jan_4",header = FALSE,sep='\t',fill=T)

l_5 =  read.table("Jan_5",header = FALSE,sep='\t',fill=T)
l_6 =  read.table("Jan_6",header = FALSE,sep='\t',fill=T)
l_7 =  read.table("Jan_7",header = FALSE,sep='\t',fill=T)

colnames(l_1)<-c('tip','total','time','lon','lat')
colnames(l_2)<-c('tip','total','time','lon','lat')
colnames(l_3)<-c('tip','total','time','lon','lat')
colnames(l_4)<-c('tip','total','time','lon','lat')
colnames(l_5)<-c('tip','total','time','lon','lat')
colnames(l_6)<-c('tip','total','time','lon','lat')
colnames(l_7)<-c('tip','total','time','lon','lat')


########### Financial District ##############


###-------1 111111
map_str <- get_map(location = "Financial District", zoom = 14)
ggmap(map_str, extent = "device") +geom_density2d(data = l_1, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_1, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Sunday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 

map_str <- get_map(location = "Financial District", zoom = 14,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_1, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_1, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Sunday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 




#############--------22222 2222
map_str <- get_map(location = "Financial District", zoom = 14)
ggmap(map_str, extent = "device") +geom_density2d(data = l_2, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_2, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Monday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 



map_str <- get_map(location = "Financial District", zoom = 14,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_2, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_2, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Monday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 


#######------------3333333
map_str <- get_map(location = "Financial District", zoom = 14)
ggmap(map_str, extent = "device") +geom_density2d(data = l_3, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_3, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Tuesday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 


map_str <- get_map(location = "Financial District", zoom = 14,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_3, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_3, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Tuesday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 



########--------44444
map_str <- get_map(location = "Financial District", zoom = 14)
ggmap(map_str, extent = "device") +geom_density2d(data = l_4, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_4, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Wednesday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 


map_str <- get_map(location = "Financial District", zoom = 14,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_4, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_4, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Wednesday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 


########--------555555555
map_str <- get_map(location = "Financial District", zoom = 14)
ggmap(map_str, extent = "device") +geom_density2d(data = l_5, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_5, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Thursday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 


map_str <- get_map(location = "Financial District", zoom = 14,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_5, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_5, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Thursday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 




########--------66666666666
map_str <- get_map(location = "Financial District", zoom = 14)
ggmap(map_str, extent = "device") +geom_density2d(data = l_6, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_6, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Friday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 


map_str <- get_map(location = "Financial District", zoom = 14,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_6, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_6, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Friday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 


########--------777777777777
map_str <- get_map(location = "Financial District", zoom = 14)
ggmap(map_str, extent = "device") +geom_density2d(data = l_7, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_7, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Saturday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 


map_str <- get_map(location = "Financial District", zoom = 14,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_7, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_7, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Saturday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 



##################### Upperwest


#------------------------- W
map_str <- get_map(location = "Manhattan", zoom = 14)
ggmap(map_str, extent = "device") +geom_density2d(data = l_4, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_4, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Wednesday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 



map_str <- get_map(location = "Manhattan", zoom = 14,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_4, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_4, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Wednesday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 



#------------------------------ Sa
map_str <- get_map(location = "Manhattan", zoom = 14)
ggmap(map_str, extent = "device") +geom_density2d(data = l_7, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_7, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Saturday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 



map_str <- get_map(location = "Manhattan", zoom = 14,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_7, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_7, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Saturday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 



##### --Friday
map_str <- get_map(location = "Manhattan", zoom = 12)
ggmap(map_str, extent = "device") +geom_density2d(data = l_3, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_3, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Overview')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 



map_str <- get_map(location = "Manhattan", zoom = 14,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_6, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_6, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Friday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 



########  New York


#####--------Friday
map_str <- get_map(location = "Manhattan", zoom = 12)
ggmap(map_str, extent = "device") +geom_density2d(data = l_6, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_6, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Friday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 



map_str <- get_map(location = "Manhattan", zoom = 12,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_6, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_6, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Friday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 




map_str <- get_map(location = "Brooklyn", zoom = 11,maptype='satellite')
ggmap(map_str, extent = "device") +geom_density2d(data = l_6, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = l_6, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red") + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)+ggtitle('Friday')+ labs(x = 'Longitude', y = 'Latitude', colour = 'Trips density') 




















map_str <- get_map(location = "Manhattan", zoom = 12,maptype = "satellite")
map_str <- get_map(location = "Financial District",maptype = "satellite", zoom = 14)
ggmap(map_str, extent = "device") +geom_density2d(data = label_data, 
                                                  aes(x = lon, y = lat), size = 0.3) + stat_density2d(data = label_data, 
                                                                                                      aes(x = lon, y = lat,fill = ..level.. , alpha = ..level..),size = 0.01, 
                                                                                                      bins = 16, geom = "polygon") + scale_fill_gradient(low = "green", high = "red",guide=FALSE) + 
  scale_alpha(range = c(0, 0.3), guide = FALSE)







