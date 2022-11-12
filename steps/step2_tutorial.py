# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from .lib.generate_images import generate_gradients, get_gradient_direction, generate_base64_image, resize_image

def render():
    images = []

    image1 = st.file_uploader("Choose front image", help="Recommended size: 710x460 pixels", key="image2")
    if image1 != None:
        images.append(image1)
        
    image2 = st.file_uploader("Choose bottom image", help="Recommended size: 710x460 pixels", key="image1")
    if image2 != None:
        images.append(image2)

    showCategory = st.checkbox('Show category text and icon?')

    direction = st.selectbox(
        'Gradient direction',
        ['0 degrees (left-to-right)',
        '45 degrees (diagonal top-left-to-bottom-right)',
        '90 degrees (top-to-bottom)',
        '135 degrees (diagonal top-right-to-bottom-left)',
        '315 degrees (diagonal bottom-left-top-top-right)'
        ],
    )
    
    return [images, showCategory, direction]


def generate(images, category, gradient_direction):
    verify_arguments(images)

    buffered_image1 = resize_image(images[0], 710, 460)
    buffered_image2 = resize_image(images[1], 710, 460)
    bottom_image = generate_base64_image(buffered_image1.getvalue())
    front_image = generate_base64_image(buffered_image2.getvalue())

    generated_images = []
    gradients = generate_gradients()
    coordinates = get_gradient_direction(gradient_direction)

    for i in range(len(gradients) - 1):
        categoryContent = ''

        if category:
            categoryContent = '<path fill-rule="evenodd" clip-rule="evenodd" d="M1212 90C1212 66.804 1230.8 48 1254 48H1390C1413.2 48 1432 66.804 1432 90C1432 113.196 1413.2 132 1390 132H1254C1230.8 132 1212 113.196 1212 90ZM1284 90C1284 106.569 1270.57 120 1254 120C1237.43 120 1224 106.569 1224 90C1224 73.4315 1237.43 60 1254 60C1270.57 60 1284 73.4315 1284 90ZM1296.95 81.0455V83.696H1302.35V98.5H1305.49V83.696H1310.88V81.0455H1296.95ZM1320.23 85.4091V92.9943C1320.23 93.6591 1320.09 94.2131 1319.81 94.6562C1319.54 95.0938 1319.19 95.4233 1318.77 95.6449C1318.34 95.8665 1317.9 95.9773 1317.44 95.9773C1316.71 95.9773 1316.11 95.733 1315.65 95.2443C1315.2 94.7557 1314.97 94.0966 1314.97 93.267V85.4091H1311.89V93.7443C1311.89 94.7898 1312.07 95.6818 1312.44 96.4205C1312.81 97.1534 1313.32 97.7131 1313.98 98.0994C1314.63 98.4801 1315.39 98.6705 1316.25 98.6705C1317.23 98.6705 1318.06 98.4375 1318.73 97.9716C1319.41 97.5057 1319.89 96.9062 1320.19 96.1733H1320.33V98.5H1323.32V85.4091H1320.23ZM1333.27 87.7955V85.4091H1330.68V82.2727H1327.6V85.4091H1325.74V87.7955H1327.6V95.0739C1327.59 95.892 1327.77 96.5739 1328.13 97.1193C1328.49 97.6648 1328.98 98.0682 1329.6 98.3295C1330.22 98.5852 1330.92 98.7017 1331.69 98.679C1332.13 98.6676 1332.5 98.6278 1332.8 98.5597C1333.1 98.4915 1333.34 98.429 1333.5 98.3722L1332.98 95.9602C1332.9 95.983 1332.77 96.0085 1332.61 96.0369C1332.45 96.0653 1332.27 96.0795 1332.08 96.0795C1331.83 96.0795 1331.59 96.0398 1331.38 95.9602C1331.17 95.8807 1331 95.733 1330.87 95.517C1330.75 95.2955 1330.68 94.9773 1330.68 94.5625V87.7955H1333.27ZM1338.33 97.9119C1339.27 98.4744 1340.38 98.7557 1341.66 98.7557C1342.93 98.7557 1344.04 98.4744 1344.98 97.9119C1345.92 97.3494 1346.64 96.5625 1347.15 95.5511C1347.67 94.5398 1347.93 93.358 1347.93 92.0057C1347.93 90.6534 1347.67 89.4688 1347.15 88.4517C1346.64 87.4347 1345.92 86.6449 1344.98 86.0824C1344.04 85.5199 1342.93 85.2386 1341.66 85.2386C1340.38 85.2386 1339.27 85.5199 1338.33 86.0824C1337.39 86.6449 1336.67 87.4347 1336.15 88.4517C1335.64 89.4688 1335.38 90.6534 1335.38 92.0057C1335.38 93.358 1335.64 94.5398 1336.15 95.5511C1336.67 96.5625 1337.39 97.3494 1338.33 97.9119ZM1343.41 95.7131C1342.95 96.0938 1342.37 96.2841 1341.67 96.2841C1340.96 96.2841 1340.37 96.0938 1339.9 95.7131C1339.43 95.3267 1339.09 94.8097 1338.85 94.1619C1338.62 93.5142 1338.51 92.7926 1338.51 91.9972C1338.51 91.196 1338.62 90.4716 1338.85 89.8239C1339.09 89.1705 1339.43 88.6506 1339.9 88.2642C1340.37 87.8778 1340.96 87.6847 1341.67 87.6847C1342.37 87.6847 1342.95 87.8778 1343.41 88.2642C1343.88 88.6506 1344.22 89.1705 1344.45 89.8239C1344.68 90.4716 1344.8 91.196 1344.8 91.9972C1344.8 92.7926 1344.68 93.5142 1344.45 94.1619C1344.22 94.8097 1343.88 95.3267 1343.41 95.7131ZM1350.79 85.4091V98.5H1353.87V90.804C1353.87 90.2472 1354 89.7557 1354.26 89.3295C1354.51 88.9034 1354.86 88.571 1355.3 88.3324C1355.75 88.0881 1356.26 87.9659 1356.82 87.9659C1357.08 87.9659 1357.35 87.9858 1357.63 88.0256C1357.92 88.0597 1358.12 88.0994 1358.25 88.1449V85.3068C1358.11 85.2784 1357.93 85.2585 1357.72 85.2472C1357.51 85.2301 1357.32 85.2216 1357.15 85.2216C1356.4 85.2216 1355.73 85.429 1355.14 85.8438C1354.56 86.2528 1354.15 86.8352 1353.92 87.5909H1353.78V85.4091H1350.79ZM1360.54 85.4091V98.5H1363.63V85.4091H1360.54ZM1360.83 83.0653C1361.19 83.3892 1361.61 83.5511 1362.09 83.5511C1362.59 83.5511 1363.01 83.3892 1363.36 83.0653C1363.71 82.7358 1363.88 82.3409 1363.88 81.8807C1363.88 81.4148 1363.71 81.0199 1363.36 80.696C1363.01 80.3665 1362.59 80.2017 1362.09 80.2017C1361.61 80.2017 1361.19 80.3665 1360.83 80.696C1360.48 81.0199 1360.3 81.4148 1360.3 81.8807C1360.3 82.3409 1360.48 82.7358 1360.83 83.0653ZM1368.57 98.321C1369.23 98.6165 1369.98 98.7642 1370.81 98.7642C1371.49 98.7642 1372.08 98.6705 1372.59 98.483C1373.1 98.2898 1373.52 98.0369 1373.86 97.7244C1374.2 97.4062 1374.46 97.0653 1374.65 96.7017H1374.75V98.5H1377.72V89.7386C1377.72 88.8693 1377.56 88.1449 1377.24 87.5653C1376.93 86.9858 1376.52 86.5284 1376 86.1932C1375.48 85.8523 1374.91 85.608 1374.29 85.4602C1373.66 85.3125 1373.03 85.2386 1372.4 85.2386C1371.49 85.2386 1370.65 85.375 1369.9 85.6477C1369.14 85.9148 1368.5 86.3182 1367.98 86.858C1367.46 87.392 1367.08 88.0568 1366.85 88.8523L1369.73 89.2614C1369.89 88.8125 1370.18 88.4233 1370.62 88.0938C1371.06 87.7642 1371.66 87.5994 1372.42 87.5994C1373.13 87.5994 1373.68 87.7756 1374.06 88.1278C1374.44 88.4801 1374.63 88.9773 1374.63 89.6193V89.6705C1374.63 89.9659 1374.52 90.1847 1374.3 90.3267C1374.09 90.4631 1373.74 90.5653 1373.26 90.6335C1372.79 90.696 1372.16 90.767 1371.4 90.8466C1370.76 90.9148 1370.14 91.0256 1369.55 91.179C1368.96 91.3267 1368.42 91.5455 1367.95 91.8352C1367.48 92.125 1367.11 92.5114 1366.84 92.9943C1366.56 93.4773 1366.43 94.0881 1366.43 94.8267C1366.43 95.6847 1366.62 96.4062 1367 96.9915C1367.38 97.5767 1367.91 98.0199 1368.57 98.321ZM1373.22 96.1307C1372.77 96.375 1372.23 96.4972 1371.61 96.4972C1370.97 96.4972 1370.44 96.3523 1370.02 96.0625C1369.61 95.7727 1369.4 95.3438 1369.4 94.7756C1369.4 94.3778 1369.51 94.054 1369.72 93.804C1369.93 93.5483 1370.21 93.3494 1370.58 93.2074C1370.94 93.0653 1371.35 92.9631 1371.81 92.9006C1372.02 92.8722 1372.26 92.8381 1372.54 92.7983C1372.82 92.7585 1373.1 92.7131 1373.38 92.6619C1373.67 92.6108 1373.92 92.5511 1374.15 92.483C1374.38 92.4148 1374.55 92.3409 1374.64 92.2614V93.804C1374.64 94.2869 1374.52 94.733 1374.27 95.142C1374.02 95.5511 1373.67 95.8807 1373.22 96.1307ZM1384.15 98.5V81.0455H1381.06V98.5H1384.15ZM1395.09 89.1761L1397.91 88.8693C1397.7 87.7557 1397.15 86.8722 1396.26 86.2188C1395.38 85.5653 1394.17 85.2386 1392.64 85.2386C1391.59 85.2386 1390.67 85.4034 1389.87 85.733C1389.07 86.0568 1388.45 86.517 1388 87.1136C1387.56 87.7045 1387.34 88.4034 1387.35 89.2102C1387.34 90.1648 1387.64 90.9545 1388.24 91.5795C1388.84 92.1989 1389.77 92.6392 1391.03 92.9006L1393.26 93.3693C1393.86 93.5 1394.31 93.6875 1394.59 93.9318C1394.88 94.1761 1395.03 94.4858 1395.03 94.8608C1395.03 95.304 1394.8 95.6761 1394.35 95.9773C1393.91 96.2784 1393.32 96.429 1392.59 96.429C1391.88 96.429 1391.3 96.2784 1390.86 95.9773C1390.42 95.6761 1390.13 95.2301 1389.99 94.6392L1386.98 94.929C1387.17 96.1335 1387.75 97.0739 1388.73 97.75C1389.7 98.4205 1390.99 98.7557 1392.6 98.7557C1393.69 98.7557 1394.65 98.5795 1395.49 98.2273C1396.34 97.875 1396.99 97.3864 1397.46 96.7614C1397.94 96.1307 1398.18 95.4034 1398.19 94.5795C1398.18 93.642 1397.88 92.8835 1397.27 92.304C1396.67 91.7244 1395.74 91.3011 1394.51 91.0341L1392.27 90.5568C1391.61 90.4034 1391.13 90.2074 1390.84 89.9688C1390.56 89.7301 1390.42 89.4205 1390.42 89.0398C1390.42 88.5966 1390.63 88.2358 1391.06 87.9574C1391.5 87.679 1392.04 87.5398 1392.68 87.5398C1393.16 87.5398 1393.56 87.6165 1393.89 87.7699C1394.22 87.9233 1394.48 88.125 1394.68 88.375C1394.88 88.625 1395.01 88.892 1395.09 89.1761Z" fill="white"/><path d="M1253.86 80.0098C1253.81 80.0191 1253.76 80.0331 1253.71 80.0517L1238.6 85.3846C1238.24 85.5083 1238 85.8456 1238 86.2248C1238 86.6039 1238.24 86.9412 1238.6 87.0652L1244.22 89.051V96.6895C1244.22 97.4564 1244.69 98.0696 1245.27 98.5089C1245.84 98.9478 1246.57 99.2845 1247.43 99.5645C1249.16 100.124 1251.46 100.453 1254 100.453C1256.54 100.453 1258.84 100.124 1260.57 99.5645C1261.44 99.2845 1262.16 98.9479 1262.74 98.5089C1263.31 98.0696 1263.78 97.4564 1263.78 96.6895V89.051L1268.22 87.4818V92.0091C1268.22 92.2472 1268.31 92.4766 1268.48 92.6458C1268.64 92.8154 1268.87 92.9106 1269.11 92.9106C1269.35 92.9106 1269.58 92.8154 1269.74 92.6458C1269.91 92.4766 1270 92.2472 1270 92.0091V86.2319C1270 85.8506 1269.76 85.5096 1269.4 85.3846L1254.29 80.0517C1254.15 80.0024 1254.01 79.9881 1253.86 80.0098H1253.86ZM1254 81.8293L1266.43 86.218L1254 90.6203L1241.56 86.2319L1254 81.8293ZM1246 89.676L1253.71 92.3982C1253.9 92.4636 1254.1 92.4636 1254.29 92.3982L1262 89.676V96.6895C1262 96.718 1261.98 96.8579 1261.65 97.1062C1261.33 97.3545 1260.75 97.631 1260.01 97.87C1258.53 98.3483 1256.39 98.6754 1254 98.6754C1251.62 98.6754 1249.47 98.3483 1247.99 97.87C1247.25 97.631 1246.67 97.3545 1246.35 97.1062C1246.02 96.8579 1246 96.718 1246 96.6895L1246 89.676Z" fill="white"/>'

        generated_images.append(f"""
            <svg width="100%" viewBox="0 0 1480 700" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g clip-path="url(#clip0_306_419)">
                    <rect width="1480" height="700" fill="url(#gradient)"/>
                    <g filter="url(#filter0_d_306_419)">
                        <path d="M987 253C987 246.373 981.627 241 975 241H247V779H987V253Z" fill="white"/>
                        <path d="M959 325C959 320.582 955.418 317 951 317H247V779H959V325Z" fill="url(#pattern1)"/>
                        <circle r="6" transform="matrix(-1 0 0 1 953 279)" fill="#FF6C6C"/>
                        <circle r="6" transform="matrix(-1 0 0 1 925 279)" fill="#FFE312"/>
                        <circle r="6" transform="matrix(-1 0 0 1 897 279)" fill="#3DD56D"/>
                    </g>
                    <g filter="url(#filter1_d_306_419)">
                        <path d="M728 162.5H0.5V699.5H739.5V174C739.5 167.649 734.351 162.5 728 162.5Z" fill="white" stroke="#FAFAFA"/>
                        <path d="M712 246C712 241.582 708.418 238 704 238H0V700H712V246Z" fill="url(#pattern2)"/>
                        <circle r="6" transform="matrix(-1 0 0 1 706 200)" fill="#FF6C6C"/>
                        <circle r="6" transform="matrix(-1 0 0 1 678 200)" fill="#FFE312"/>
                        <circle r="6" transform="matrix(-1 0 0 1 650 200)" fill="#3DD56D"/>
                    </g>

                    # Category text and icon
                    {categoryContent}
                </g>

                <defs>
                    <filter id="filter0_d_306_419" x="207" y="205" width="804" height="602" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_306_419"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_306_419" result="shape"/>
                    </filter>
                    <pattern id="pattern1" patternContentUnits="objectBoundingBox" width="1" height="1">
                        <use xlink:href="#screenshot-1" transform="translate(-0.000627131) scale(0.00114542 0.00156006)"/>
                    </pattern>
                    <filter id="filter1_d_306_419" x="-40" y="126" width="804" height="602" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_306_419"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_306_419" result="shape"/>
                    </filter>
                    <pattern id="pattern2" patternContentUnits="objectBoundingBox" width="1" height="1">
                        <use xlink:href="#screenshot-2" transform="translate(-0.09 -0.004) scale(0.00114359 0.00170173)" />
                    </pattern>
                    <clipPath id="clip0_306_419">
                        <rect width="1480" height="700" fill="white"/>
                    </clipPath>
                    # Gradient
                    <linearGradient id="gradient" x1="0" y1="0" x2="1" y2="0" gradientTransform="rotate({coordinates[0]})">{gradients[i]}</linearGradient>
                    # Screenshots
                    <image id="screenshot-1" width="1063" height="588" xlink:href="data:image/jpeg;charset=utf-8;base64,{front_image}" />
                    <image id="screenshot-2" width="1063" height="588" xlink:href="data:image/jpeg;charset=utf-8;base64,{bottom_image}" />
                </defs>
            </svg>
        """.strip())
    
    return generated_images

def verify_arguments(images):
    MIN_IMAGES = 2

    if len(images) < MIN_IMAGES:
        st.error("Please add at least two images")
        st.stop()