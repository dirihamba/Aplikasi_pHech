import streamlit as st # type: ignore
test = st.sidebar.selectbox("Navigation", ['Beranda', 'Tentang pH','Video Simulasi'])
with st.sidebar.container():
        st.sidebar.markdown("pHech - Aplikasi Perhitungan pH")


  
if test == "Beranda":
    st.title(':violet[Aplikasi penentuan pH Larutan]')
    st.markdown('''Selamat datang di web kami.👩🏻‍🔬''')
    st.markdown('''Aplikasi ini dapat digunakan untuk menentukan nilai pH dari suatu larutan atau sampel dengan menginput konsentrasi dengan satuan Molaritas.''')


    tab1,tab2=st.tabs(['Penentuan Nilai pH', 'Indikator'])

    with tab1:
        st.header('Penentuan Nilai pH')
        import pandas as pd
        st.write('Beberapa contoh larutan serta jenisnya')
        data={'Nama Larutan':['NaOH','KOH','LiOH','RbOH','Ba(OH)2','Ca(OH)2','Pb(OH)2','Cu(OH)2','NaHCO3','HBO3','Fe(OH)2','NH4OH','Zn(OH)2','HCl','HI','HClO3','HClO4','H2SO4','HBr','H2C2O4','H3PO4','CH3COOH','H2O2','H2CO3','HCN'],
              'Jenis larutan':['Basa Kuat','Basa Kuat','Basa Kuat','Basa Kuat','Basa Kuat','Basa Kuat','Basa Lemah','Basa Lemah','Basa Lemah','Basa Lemah','Basa Lemah','Basa Lemah','Basa Lemah','Asam Kuat','Asam Kuat','Asam Kuat','Asam Kuat','Asam Kuat','Asam Kuat','Asam Lemah','Asam Lemah','Asam Lemah','Asam lemah','Asam Lemah','Asam Lemah']}
        
        df=pd.DataFrame(data)

        df


        st.write('Nama Larutan yang akan dihitung pH-nya:')
        NamaLarutan=st.selectbox('Nama Larutan',("NaOH","KOH","LiOH","RbOH","Ba(OH)2","Ca(OH)2","Pb(OH)2","Cu(OH)2","NaHCO3","HBO3","Fe(OH)2","NH4OH","Zn(OH)2","HCl","HI","HClO3","HClO4","H2SO4","HBr","H2C2O4","H3PO4","CH3COOH","H2O2","H2CO3","HCN"))
       
        st.write('Silahkan pilih jenis larutan dengan format "Asam Kuat", "Basa Kuat", "Asam Lemah", "Basa Lemah"')
        option=st.selectbox('Jenis Larutan',("Asam Kuat", "Basa Kuat", "Asam Lemah", "Basa Lemah"))

        if option=="Asam Kuat":   
            jumlah_digit=4
            cons = st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
            jumlah_digit1=4
            val = st.number_input(f'Masukkan valensi larutan', format='%.'+str(jumlah_digit)+'f')
            H = cons * val
            import numpy as np
            pH = -(np.log10(H))

            if  st.button('Hitung'):
                st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                st.subheader(f':green[{round(pH,2)}]')
                st.balloons()
            else :
                st.write()

        elif option=="Basa Kuat": 
            jumlah_digit=4 
            cons= st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')
            jumlah_digit1=4 
            val = st.number_input(f'Masukan valensi larutan', format='%.'+str(jumlah_digit)+'f')
            OH = cons * val 
            import numpy as np
            POH = (np.log10(OH))
            pH = 14-POH
            if st.button('Hitung'):
                st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                st.subheader(f':green[{round(pH,2)}]')
                st.snow()
            else :
                st.write()

        elif option=="Asam Lemah": 
            jumlah_digit=4
            cons=st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f') 
            a = cons * (1.8 * 10**(-5))
            import numpy as np
            H = np.sqrt(a)
            pH = -(np.log10(H))
            if st.button('Hitung'):
                st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                st.subheader(f':green[{round(pH,2)}]')
                st.balloons()
            else :
                st.write()

        elif option=="Basa Lemah": 
            jumlah_digit=4
            cons=st.number_input(f'Masukkan konsentrasi larutan dalam Molaritas (M)', format='%.'+str(jumlah_digit)+'f')  
            a = cons* (1.8 * 10**(-5))
            import numpy as np 
            OH = np.sqrt(a)
            POH = - (py.log10(OH))
            pH = 14 - POH
            if st.button('Hitung'):
                st.write('pH Larutan', NamaLarutan, 'yang merupakan', option, 'adalah')
                st.subheader(f':green[{round(pH,2)}]')
                st.snow()
            else :
                st.write()



    with tab2:
        st.header("Penentuan indikator")
        jumlah_digit=1
        pH=st.number_input('Masukkan nilai pH Anda (range 1 - 14):',float(jumlah_digit))

        if st.button('Submit'):
            if 1.0<=pH<=4.4 :
                st.write('Indikator yang cocok pada pH',pH,'adalah')
                st.subheader(":orange[Sindur Metil (SM)]")
                g1, g2, g3 = st.columns([1,2,1])
                with g1:
                    st.write(" ")
                with g3:
                    st.write(" ")
                with g2:
                    st.image('https://th.bing.com/th/id/R.1ea82b6df89b35a6862be0f12abf40a0?rik=YcdwyCI2TwToBg&riu=http%3a%2f%2fimages.fineartamerica.com%2fimages-medium-large%2fmethyl-orange-indicator-andrew-lambert-photography.jpg&ehk=VWeVt5uMRVCFWPfjbZLC80ETLIUMYPCCDvbl3CQKUzU%3d&risl=&pid=ImgRaw&r=0')

                st.write("---")

                st.subheader('Fakta Mengenai Sindur Metil(SM)')
 
                st.write('''Indikator sindur metil (SM) adalah suatu senyawa organometalik yang digunakan sebagai indikator pH pada larutan asam atau netral dalam rentang pH 3,1 - 4,4. Berikut adalah beberapa fakta menarik tentang indikator sindur metil:''')
                
                st.write(':green[Kelebihan:]')
                st.write('1. Indikator sindur metil memiliki rentang perubahan warna yang akurat, sehingga sangat cocok digunakan dalam analisis kuantitatif.')
                st.write('2. Senyawa ini tidak bersifat toksik dan mudah digunakan, sehingga teramasuk aman untuk digunakan dalam laboratorium')
                st.write('3. Sifatnya yang stabil baik terhadap cahaya dan panas, sehingga dapat bertahan dalam jangka waktu yang lama')

                st.write(':green[Kekurangan:]')
                st.write('1. Rentang pH yang dapat diukur terbatas pada lingkungan yang bersifat basa.')
                st.write('2. Indikator ini tidak dapat digunakan dalam suasana larutan yang sangat asam dan sangat basa, karena warnanya tidak berubah.')
                st.write('3. Indikator ini rentan terhadap oksidasi dan degradasi(pencampuran), sehingga perlu disimpan dengan hati-hati serta penggunaan dalam waktu singkat setelah dibuka.')
                
            elif 4.2 <=pH <=6.3:
                st.write('indikator yang cocok pada pH',pH,'adalah')
                st.subheader(":red[Metil Merah (MM)]")
                g1, g2, g3 = st.columns([1,2,1])
                with g1:
                    st.write(" ")
                with g3:
                    st.write(" ")
                with g2:
                    st.image('https://media.sciencephoto.com/image/c0527725/800wm/C0527725-Methyl_red_indicator.jpg')
                st.write("---")
                st.subheader('Fakta Mengenai Metil Merah (MM)')
                
                st.write('''Indikator metil merah (MM) adalah senyawa organik yang digunakan sebagai indikator pH pada larutan asam dan netral dalam rentang pH 4,2 - 6,3. Berikut adalah beberapa fakta menarik tentang indikator metil merah:''')

                st.write(':green[Kelebihan :]')
                st.write('1. Indikator metil merah memiliki perubahan warna yang sangat kontras dan mudah diamati, sehingga sangat mudah digunakan dalam laboratorium.')
                st.write('2. Senyawa ini memiliki harga yang terjangkau dan mudah ditemukan, sehingga sangat populer di laboratorium.')
                st.write('3. Indikator metil merah mudah larut dalam air dan pelarut organik lainnya, sehingga dapat digunakan pada berbagai jenis larutan.')

                st.write(':green[Kekurangan :]')
                st.write('1. Tidak cocok untuk digunakan dalam analisis pH lingkungan yang bersifat basa.')
                st.write('2. Senyawa ini memiliki kelemahan yaitu rentan terhadap degradasi oleh cahaya dan panas, sehingga perlu disimpan dengan hati-hati dan digunakan dalam waktu yang singkat setelah dibuka.')
                st.write('3. Indikator metil merah rentan terhadap interferensi oleh ion logam seperti Fe3+ dan Al3+, sehingga perlu dilakukan kalibrasi kembali saat digunakan pada larutan yang mengandung ion logam tersebut.')

            elif 6.0 <= pH <=7.6 :
                st.write('Indikator yang cocok pada pH', pH, 'adalah')
                st.subheader(":blue[Bromtimol Biru (BTB)]")
                g1, g2, g3 = st.columns([1,2,1])
                with g1:
                    st.write(" ")
                with g3:
                    st.write(" ")
                with g2:
                    st.image("https://media.sciencephoto.com/image/c0440287/800wm/C0440287-Bromothymol_blue_indicator.jpg")
                st.write("---")
                st.subheader('Fakta Bromtimol Biru (BTB)')

                st.write('''Indikator bromtimol blue (BTB) adalah senyawa organik yang digunakan sebagai indikator pH pada larutan netral dan bersifat asam dalam rentang pH 6,0-7,6. Berikut adalah beberapa fakta menarik tentang indikator bromtimol blue:''')

                st.write(''':green[Kelebihan : ]''')
                st.write('1. Indikator bromtimol blue memiliki perubahan warna yang tajam dan mudah diamati, sehingga sangat mudah digunakan dalam laboratorium.')
                st.write('2. Rentang perubahan warna indikator bromtimol blue sangat sempit, sehingga cocok untuk digunakan dalam analisis kuantitatif.')
                st.write('3. Indikator bromtimol blue mudah larut dalam air dan pelarut organik lainnya, sehingga dapat digunakan pada berbagai jenis larutan.')

                st.write(''':green[Kekurangan : ]''')
                st.write('1. Rentang pH yang dapat diukur oleh indikator bromtimol blue terbatas pada lingkungan netral dan asam, sehingga tidak cocok untuk digunakan dalam analisis pH lingkungan yang bersifat basa.')
                st.write('2. Senyawa ini memiliki kelemahan yaitu sensitivitas yang rendah terhadap perubahan pH pada lingkungan yang bersifat basa.')
                st.write('3. Indikator bromtimol blue rentan terhadap interferensi oleh ion logam seperti Fe3+ dan Al3+, sehingga perlu dilakukan kalibrasi kembali saat digunakan pada larutan yang mengandung ion logam tersebut.')
                
            elif 8.0 <= pH <=14 :
                st.write('Indikator yang cocok pada pH', pH, 'adalah')
                st.subheader(":blue[Fenolftalein (PP)]")  
                g1, g2, g3 = st.columns([1,2,1])
                with g1:
                    st.write(" ")
                with g3:
                    st.write(" ")
                with g2:
                    st.image('https://media.sciencephoto.com/image/c0391215/800wm/C0391215-Phenolphthalein_Indicator.jpg')             
                st.write("---")
                st.subheader('Fenolftalein (PP)')

                st.write('Indikator fenolftalein (PP) adalah senyawa organik yang digunakan sebagai indikator pH pada larutan bersifat basa dalam rentang pH 8,0-10. Berikut adalah beberapa fakta menarik tentang indikator fenolftalein:')

                st.write(''':green[Kelebihan : ]''')
                st.write('1. Indikator fenolftalein memiliki perubahan warna yang tajam dan mudah diamati, sehingga sangat mudah digunakan dalam laboratorium.')
                st.write('2. Rentang perubahan warna indikator fenolftalein sangat sempit, sehingga cocok untuk digunakan dalam analisis kuantitatif.')
                st.write('3. Indikator fenolftalein mudah larut dalam air dan pelarut organik lainnya, sehingga dapat digunakan pada berbagai jenis larutan.')

                st.write(''':green[Kekurangan : ]''')
                st.write('1. Tidak cocok untuk digunakan dalam analisis pH lingkungan yang bersifat netral atau asam.')
                st.write('2. Senyawa ini memiliki kelemahan yaitu sensitivitas yang rendah terhadap perubahan pH pada lingkungan yang bersifat netral atau asam.')
                st.write('3. Indikator fenolftalein rentan terhadap interferensi oleh ion logam seperti Fe3+ dan Al3+, sehingga perlu dilakukan kalibrasi kembali saat digunakan pada larutan yang mengandung ion logam tersebut.')

            else:
                st.error('Nilai yang Anda masukkan salah. Input kembali dalam range 3.1-10')

if test == "Tentang pH":
    st.title(':green[Mari Cari Tahu Apa Itu pH]')
    st.caption('Halaman ini berisi pengertian mengenai pH, skala pada pH, alat ukur untuk menghitung pH, dan contoh pada tiap-tiap nilai pH')

    tab1, tab2, tab3, tab4, = st.tabs(["Mengenai pH", "Skala pH", "Alat ukur","Contoh pH"])

    with tab1:
        st.header(':red[Pengertian pH]')
        g1, g2, g3 = st.columns([1,2,1])
        with g1:
            st.write(" ")
        with g3:
            st.write(" ")
        with g2:
            st.image("https://sciencenotes.org/wp-content/uploads/2022/02/Bronsted-Lowry-Acid-and-Base.png",width=300)
            st.caption("Asam Bronsted Lowry adalah donor proton atau hidrogen, sedangkan basa Bronsted Lowry adalah akseptor proton atau hidrogen.")

        st.write('Menurut Bronsted-Lowry, asam adalah sebagai donor proton(pemberi ion H+) sedangkan basa sebagai akseptor proton(penerima ion H+). pH merupakan derajat keasaman yang digunakan untuk menyatakan tingkat keasaman atau kebasaan yang dimiliki oleh suatu larutan yang didefinisikan sebagai kologartitma aktivitas ion hidrogen (H+) yang terlarut. Koefisien aktivitas ion hidrogen tidak dapat diukur secara eksperimental, sehingga nilainya didasarkan pada perhitungan teoritis. Skala pH bukanlah skala absolut melainkan bersifat relatif.')
        st.write('Istilah “pH” berasal dari kata Jerman “potenz,” yang berarti “pangkat” , dikombinasikan dengan H, simbol unsur untuk hidrogen, jadi pH adalah singkatan dari “Pangkat Hidrogen".Pengertian pada umumnya, pH (Power of Hydrogen) adalah skala yang digunakan untuk menyatakan tingkat keasaman atau kebasaan yang dimiliki oleh suatu larutan. Skala dari pH terdiri dari angka 1 hingga 14.')
        st.write('Pada pengukuran skala pH, terdapat tiga jenis parameter yaitu pH asam, netral, dan basa. Suatu larutan dikatakan asam jika terdapat ion H+ yang lebih banyak daripada ion OH–. Asam memiliki pH<7. Bersifat netral jika jumlah ion H+ dan OH– sama dalam larutan. Larutan netral memiliki pH 7. Dan larutan basa jika terdapat jumlah ion OH– lebih banyak dibanding H+, basa memiliki pH>7.')
        st.write("---")

    with tab2:
        st.header(':red[Skala pH]')
        g1, g2, g3 = st.columns([1,2,1])
        with g1:
            st.write(" ")
        with g3:
            st.write(" ")
        with g2:
            st.image("https://media.istockphoto.com/vectors/ph-scale-balance-liquid-level-litmus-color-change-indicator-of-and-vector-id1400164115?k=20&m=1400164115&s=170667a&w=0&h=3Ao8EMXYnkG1QMR2pbNvImYPCpvBE__vksDhySORsZE=")
        st.markdown('<div style="text-align:justify">pH adalah singkatan dari "potential of hydrogen" atau "power of hydrogen". PH adalah ukuran konsentrasi ion hidrogen dalam air. Dalam kimia, pH adalah pengukuran konsentrasi ion hidrogen dalam larutan berbasis air. Ia menjadi ukuran keasaman atau kebasaan suatu larutan berair atau cairan lainnya.</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:justify">Skala pH merupakan perbandingan jarak pada gambar (literatur) dengan hasil pengujian, dimana pengujian dilakukan dengan menguji sampel menggunakan alat ukur pH, skala pH berfungsi sebagai tolak ukur penentuan asam atau basa nya suatu contoh/sampel.</div>', unsafe_allow_html=True)


    with tab3:
        st.header(':red[Indikator pH Universal]')
        g1, g2, g3 = st.columns([1,2,1])
        with g1:
            st.write(" ")
        with g3:
            st.write(" ")
        with g2:
            st.image("https://www.pakarkimia.com/wp-content/uploads/2020/05/INDIKATOR-UNIVERSAL.jpg")
            st.caption('Indikator pH Universal.')
        st.write('Indikator pH Universal Indikator pH universal merupakan indikator yang mempunyai warna standar yang berbeda untuk setiap nilai pH 1-14. Fungsi indikator universal adalah untuk memeriksa derajat keasaman suatu zat secara akurat.')
        
        st.header(':red[Lakmus]')
        g1, g2, g3 = st.columns([1,2,1])
        with g1:
            st.write(" ")
        with g3:
            st.write(" ")
        with g2:
            st.image("https://www.sentrakalibrasiindustri.com/wp-content/uploads/2023/05/perbedaan-kertas-lakmus-biru-dan-merah.jpg")
            st.caption('Kertas Lakmus Merah dan Biru')
        st.write('Kertas lakmus adalah alat yang digunakan untuk menguji apakah suatu zat bersifat asam atau basa. Ketika suatu zat dilarutkan dalam air, larutan yang dihasilkan menyebabkan kertas lakmus berubah warna. Jika dalam keadaan asam berarti memerahkan kertas lakmus biru, sedangkan dalam keadaan basa membirukan lakmus merah.')

        st.header(':red[pH Meter]')
        g1, g2, g3 = st.columns([1,2,1])
        with g1:
            st.write(" ")
        with g3:
            st.write(" ")
        with g2:
            st.image("https://img.medicalexpo.com/images_me/photo-g/100041-16315454.jpg")
            st.caption('pH Meter')
        st.write('pH meter adalah alat yang digunakan untuk mengukur tingkat asam-basa suatu larutan. Alat ini digunakan di laboratorium untuk mengukur derajat keasaman (pH) suatu larutan, apakah larutan tersebut tergolong asam, basa atau netral. pH meter mengukur perbedaan potensial antara elektroda gelas dan elektroda pembanding kemudian mengonversinya menjadi pembacaan pH yang dihitung menggunakan persamaan (4) dengan suhu (T) dalam satuan Kelvin atau persamaan (5) dengan suhu (t) dalam °C.')
    
    with tab4:
        st.header(':red[Contoh nilai pH pada kehidupan sehari-hari]')
        g1, g2, g3 = st.columns([1,2,1])
        with g1:
            st.write(" ")
        with g3:
            st.write(" ")
        with g2:
            st.image("https://4.bp.blogspot.com/-x8-QOocVqZs/WLGhD4eY3zI/AAAAAAAAAPk/vjgPxYdRUPkRgSa2Am4o-jMt9GxIwrfCwCLcB/s640/Ph%2BLevels%2BOf%2BFruits%2BAnd%2BVegetables%2B2.jpg")
        st.write('Nilai pH dapat dijumpai dalam kehidupan sehari-hari, terutama dalam bahan pangan dan kebutuhan utama lainnya. Asam merupakan salah satu penyusun dari berbagai bahan makanan dan minuman. Beberapa contoh diantaranya cuka, keju, kopi, buah-buahan, minuman bersoda, berkarbonasi dan berenergi. Hal itu dikarenakan keasaman soda terdapat pada pH 3 atau lebih rendah yang berasal dari konversi CO2 terlarut menjadi H2O sehingga menghasilkan HCO3 dan H+.')
        st.write('Zat netral dalam pH adalah mereka yang memiliki potensi hidrogen (pH) sama dengan 7. Contoh pH netral dapat dijumpai pada air keran, air sungai, air mata air langsung. Basa adalah suatu senyawa yang jika dilarutkan dalam air (larutan) dapat melepaskan ion hidroksida (OH-). Oleh karena itu, semua rumus kimia basa umumnya mengandung gugus OH.Dalam keadaan murni, basa umumnya berupa kristal padat dan bersifat kaustik. Beberapa produk rumah tangga seperti deodoran, obat maag (antacid) dan sabun serta deterjen mengandung basa.')
        st.write('Keseimbangan asam basa jaringan tubuh dan darah manusia harus berada pada pH 7,3 – 7,5 artinya kondisi tubuh bersifat agak basa atau alkalin, agar tetap sehat dan berfungsi optimal. Di atas pH 7,8 atau di bawah pH 6,8 akan menimbulkan gangguan metabolisme, yang pada akhirnya juga gangguan pada kesehatan. Untuk menjaga kondisi tubuh tersebut, sebaiknya komposisi menu terdiri dari 70% makanan pembentuk basa (alkaline forming food) dan 30% makanan pembentuk asam (acid forming food).')

if test =='Video Simulasi':
    st.title('Video simulasi titrasi')
    st.video(controls src = "video simulasi.mp4")










    