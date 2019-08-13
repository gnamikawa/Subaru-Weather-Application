#!/bin/bash
export CameraDir=/home/www/script/cwanim

export FigurebotDir=../figurebot
export WebpageImageDir=../website/build/images
export WebpageDataDir=../website/build/data
export WebpageDirBuildDir=../website/build

export WebsiteDeployPath=/home/genzo/public_html/Weather

# Collect images from security cameras
echo "[Collecting camera images]"
cp -v "$CameraDir/cw66.gif" "$WebpageImageDir" # Northwest
cp -v "$CameraDir/cw68.gif" "$WebpageImageDir" # Northeast
cp -v "$CameraDir/cw70.gif" "$WebpageImageDir" # Southeast
cp -v "$CameraDir/cw72.gif" "$WebpageImageDir" # Southwest
echo "[Done]"

# Collect graphs from python scripts
echo "[Collecting graphs]"
# cp -v "$FigurebotDir/Output/Temperature.png" "$WebpageImageDir"
# cp -v "$FigurebotDir/Output/Humidity.png" "$WebpageImageDir"
cp -av "$FigurebotDir/Output/." "$WebpageImageDir"
echo "[Done]"

# Collect data from python scripts
echo "[Collecting snapshot data]"
cp -av "$FigurebotDir/Data/." "$WebpageDataDir"
echo "[Done]"

# Collect data from python scripts
echo "[Moving website data]"
cp -av "$WebpageDirBuildDir/." "$WebsiteDeployPath"
echo "[Done]"