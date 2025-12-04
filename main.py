import tkinter as tk
from tkinter import ttk


class MovieApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('영화 예매 프로그램')
        self.root.geometry('960x680')
        self.root.configure(bg='#0f141a')

        self.users = []
        self.current_user = None
        self.admin_signed = False
        self.bookings = []
        self.movie_counter = 1
        self.movies = []
        self._seed_movies()

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Card.TFrame', background='#1c252f', relief='flat')
        self.style.configure('Title.TLabel', background='#0f141a', foreground='white', font=('맑은 고딕', 18, 'bold'))
        self.style.configure('Section.TLabel', background='#1c252f', foreground='white', font=('맑은 고딕', 12, 'bold'))
        self.style.configure('Body.TLabel', background='#1c252f', foreground='#d5d9de', font=('맑은 고딕', 10))
        self.style.configure('Accent.TButton', background='#3b82f6', foreground='white', font=('맑은 고딕', 10, 'bold'))
        self.style.map('Accent.TButton', background=[('active', '#2563eb')])
        self.style.configure('Ghost.TButton', background='#1c252f', foreground='white', borderwidth=1, relief='ridge')
        self.style.map('Ghost.TButton', background=[('active', '#24303d')])

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=12, pady=12)

        self.user_tab = ttk.Frame(self.notebook, style='Card.TFrame')
        self.admin_tab = ttk.Frame(self.notebook, style='Card.TFrame')
        self.notebook.add(self.user_tab, text='사용자')
        self.notebook.add(self.admin_tab, text='관리자')

        self._build_user_tab()
        self._build_admin_tab()
        self.root.mainloop()

    def _seed_movies(self):
        presets = [
            {'title': '별빛 무대', 'time': '14:00', 'rating': '12세 관람가'},
            {'title': '모노레일', 'time': '17:20', 'rating': '15세 관람가'},
            {'title': '밤의 파도', 'time': '20:00', 'rating': '청소년 관람불가'},
        ]
        for item in presets:
            self._add_movie_entry(item['title'], item['time'], item['rating'])

    def _add_movie_entry(self, title, show_time, rating):
        seats = {}
        rows = ['A', 'B', 'C', 'D']
        cols = ['1', '2', '3', '4', '5']
        for r in rows:
            for c in cols:
                seats[f'{r}{c}'] = ''
        self.movies.append({
            'id': self.movie_counter,
            'title': title,
            'time': show_time,
            'rating': rating,
            'seats': seats,
        })
        self.movie_counter += 1

    def _build_user_tab(self):
        header = ttk.Label(self.user_tab, text='오늘의 상영작을 선택하고 좌석을 고르세요', style='Title.TLabel')
        header.pack(anchor='w', padx=18, pady=10)

        top = ttk.Frame(self.user_tab, style='Card.TFrame')
        top.pack(fill='x', padx=12)

        auth_frame = ttk.Frame(top, style='Card.TFrame')
        auth_frame.pack(side='left', fill='x', expand=True, padx=(0, 8))

        ttk.Label(auth_frame, text='회원가입', style='Section.TLabel').grid(row=0, column=0, sticky='w', pady=(6, 2))
        self.reg_name = ttk.Entry(auth_frame)
        self.reg_email = ttk.Entry(auth_frame)
        self.reg_phone = ttk.Entry(auth_frame)
        self.reg_pw = ttk.Entry(auth_frame, show='*')
        ttk.Label(auth_frame, text='이름', style='Body.TLabel').grid(row=1, column=0, sticky='w')
        self.reg_name.grid(row=2, column=0, sticky='we', pady=(0, 6))
        ttk.Label(auth_frame, text='이메일', style='Body.TLabel').grid(row=3, column=0, sticky='w')
        self.reg_email.grid(row=4, column=0, sticky='we', pady=(0, 6))
        ttk.Label(auth_frame, text='연락처', style='Body.TLabel').grid(row=5, column=0, sticky='w')
        self.reg_phone.grid(row=6, column=0, sticky='we', pady=(0, 6))
        ttk.Label(auth_frame, text='비밀번호', style='Body.TLabel').grid(row=7, column=0, sticky='w')
        self.reg_pw.grid(row=8, column=0, sticky='we', pady=(0, 8))
        ttk.Button(auth_frame, text='가입하기', style='Accent.TButton', command=self._register_user).grid(row=9, column=0, sticky='we', pady=(0, 10))
        auth_frame.columnconfigure(0, weight=1)

        login_frame = ttk.Frame(top, style='Card.TFrame')
        login_frame.pack(side='left', fill='x', expand=True, padx=(8, 0))

        ttk.Label(login_frame, text='로그인', style='Section.TLabel').grid(row=0, column=0, sticky='w', pady=(6, 2))
        self.login_email = ttk.Entry(login_frame)
        self.login_pw = ttk.Entry(login_frame, show='*')
        ttk.Label(login_frame, text='이메일', style='Body.TLabel').grid(row=1, column=0, sticky='w')
        self.login_email.grid(row=2, column=0, sticky='we', pady=(0, 6))
        ttk.Label(login_frame, text='비밀번호', style='Body.TLabel').grid(row=3, column=0, sticky='w')
        self.login_pw.grid(row=4, column=0, sticky='we', pady=(0, 8))
        ttk.Button(login_frame, text='로그인하기', style='Accent.TButton', command=self._login_user).grid(row=5, column=0, sticky='we')
        login_frame.columnconfigure(0, weight=1)

        self.user_info = ttk.Label(self.user_tab, text='로그인 후 예매가 가능합니다', style='Body.TLabel')
        self.user_info.pack(anchor='w', padx=18, pady=(8, 10))

        content = ttk.Frame(self.user_tab, style='Card.TFrame')
        content.pack(fill='both', expand=True, padx=12, pady=(0, 12))

        movie_card = ttk.Frame(content, style='Card.TFrame')
        movie_card.pack(side='left', fill='both', expand=True, padx=(0, 8), pady=8)
        ttk.Label(movie_card, text='상영작', style='Section.TLabel').pack(anchor='w', padx=12, pady=(10, 6))
        columns = ('time', 'rating')
        self.movie_table = ttk.Treeview(movie_card, columns=columns, show='headings', height=10)
        self.movie_table.heading('time', text='시간')
        self.movie_table.heading('rating', text='등급')
        self.movie_table.column('time', width=80)
        self.movie_table.column('rating', width=100)
        self.movie_table.pack(fill='both', expand=True, padx=12, pady=(0, 12))
        self.movie_table.bind('<<TreeviewSelect>>', self._select_movie)

        seat_card = ttk.Frame(content, style='Card.TFrame')
        seat_card.pack(side='left', fill='both', expand=True, padx=(8, 0), pady=8)
        ttk.Label(seat_card, text='좌석 선택', style='Section.TLabel').pack(anchor='w', padx=12, pady=(10, 6))
        self.seat_grid = ttk.Frame(seat_card, style='Card.TFrame')
        self.seat_grid.pack(padx=12, pady=6)
        self.selected_movie_id = None

        booking_card = ttk.Frame(self.user_tab, style='Card.TFrame')
        booking_card.pack(fill='both', expand=True, padx=12, pady=(0, 12))
        ttk.Label(booking_card, text='나의 예매 내역', style='Section.TLabel').pack(anchor='w', padx=12, pady=(10, 6))
        b_columns = ('movie', 'seat', 'status')
        self.booking_table = ttk.Treeview(booking_card, columns=b_columns, show='headings', height=6)
        for col, text in zip(b_columns, ['영화', '좌석', '상태']):
            self.booking_table.heading(col, text=text)
            self.booking_table.column(col, width=160)
        self.booking_table.pack(fill='both', expand=True, padx=12, pady=(0, 10))
        ttk.Button(booking_card, text='예매 취소', style='Ghost.TButton', command=self._cancel_booking).pack(anchor='e', padx=12, pady=(0, 10))

        self.status = ttk.Label(self.user_tab, text='', style='Body.TLabel')
        self.status.pack(anchor='w', padx=18, pady=(0, 8))
        self._refresh_movies()

    def _build_admin_tab(self):
        header = ttk.Label(self.admin_tab, text='관리자 공간에서 상영작과 예매를 관리하세요', style='Title.TLabel')
        header.pack(anchor='w', padx=18, pady=10)

        login_box = ttk.Frame(self.admin_tab, style='Card.TFrame')
        login_box.pack(fill='x', padx=12, pady=(0, 10))
        ttk.Label(login_box, text='관리자 로그인', style='Section.TLabel').grid(row=0, column=0, sticky='w', pady=(6, 2))
        self.admin_email = ttk.Entry(login_box)
        self.admin_pw = ttk.Entry(login_box, show='*')
        ttk.Label(login_box, text='이메일', style='Body.TLabel').grid(row=1, column=0, sticky='w')
        self.admin_email.grid(row=2, column=0, sticky='we', pady=(0, 6))
        ttk.Label(login_box, text='비밀번호', style='Body.TLabel').grid(row=3, column=0, sticky='w')
        self.admin_pw.grid(row=4, column=0, sticky='we', pady=(0, 8))
        ttk.Button(login_box, text='로그인', style='Accent.TButton', command=self._admin_login).grid(row=5, column=0, sticky='we', pady=(0, 10))
        login_box.columnconfigure(0, weight=1)

        self.admin_state = ttk.Label(self.admin_tab, text='관리자 로그인이 필요합니다', style='Body.TLabel')
        self.admin_state.pack(anchor='w', padx=18, pady=(0, 10))

        body = ttk.Frame(self.admin_tab, style='Card.TFrame')
        body.pack(fill='both', expand=True, padx=12, pady=10)

        movie_manage = ttk.Frame(body, style='Card.TFrame')
        movie_manage.pack(side='left', fill='both', expand=True, padx=(0, 8))
        ttk.Label(movie_manage, text='상영작 관리', style='Section.TLabel').pack(anchor='w', padx=12, pady=(10, 6))
        m_columns = ('time', 'rating')
        self.admin_movie_table = ttk.Treeview(movie_manage, columns=m_columns, show='headings', height=10)
        self.admin_movie_table.heading('time', text='시간')
        self.admin_movie_table.heading('rating', text='등급')
        self.admin_movie_table.column('time', width=80)
        self.admin_movie_table.column('rating', width=100)
        self.admin_movie_table.pack(fill='both', expand=True, padx=12, pady=(0, 10))

        add_frame = ttk.Frame(movie_manage, style='Card.TFrame')
        add_frame.pack(fill='x', padx=12, pady=(0, 12))
        ttk.Label(add_frame, text='제목', style='Body.TLabel').grid(row=0, column=0, sticky='w')
        ttk.Label(add_frame, text='시간', style='Body.TLabel').grid(row=0, column=1, sticky='w')
        ttk.Label(add_frame, text='등급', style='Body.TLabel').grid(row=0, column=2, sticky='w')
        self.new_title = ttk.Entry(add_frame)
        self.new_time = ttk.Entry(add_frame)
        self.new_rating = ttk.Entry(add_frame)
        self.new_title.grid(row=1, column=0, sticky='we', padx=(0, 6))
        self.new_time.grid(row=1, column=1, sticky='we', padx=6)
        self.new_rating.grid(row=1, column=2, sticky='we', padx=(6, 0))
        ttk.Button(add_frame, text='상영 등록', style='Accent.TButton', command=self._add_movie_admin).grid(row=2, column=0, columnspan=3, sticky='we', pady=(8, 0))
        ttk.Button(add_frame, text='상영 삭제', style='Ghost.TButton', command=self._remove_movie).grid(row=3, column=0, columnspan=3, sticky='we', pady=(6, 0))
        add_frame.columnconfigure(0, weight=1)
        add_frame.columnconfigure(1, weight=1)
        add_frame.columnconfigure(2, weight=1)

        booking_manage = ttk.Frame(body, style='Card.TFrame')
        booking_manage.pack(side='left', fill='both', expand=True, padx=(8, 0))
        ttk.Label(booking_manage, text='예매 관리', style='Section.TLabel').pack(anchor='w', padx=12, pady=(10, 6))
        a_columns = ('user', 'movie', 'seat', 'status')
        self.admin_booking_table = ttk.Treeview(booking_manage, columns=a_columns, show='headings', height=16)
        for col, text in zip(a_columns, ['사용자', '영화', '좌석', '상태']):
            self.admin_booking_table.heading(col, text=text)
            self.admin_booking_table.column(col, width=120)
        self.admin_booking_table.pack(fill='both', expand=True, padx=12, pady=(0, 12))

        self._refresh_admin()

    def _register_user(self):
        name = self.reg_name.get().strip()
        email = self.reg_email.get().strip()
        phone = self.reg_phone.get().strip()
        password = self.reg_pw.get().strip()
        if not name or not email or not phone or not password:
            self._set_status('모든 정보를 입력해 주세요')
            return
        for user in self.users:
            if user['email'] == email:
                self._set_status('이미 가입된 이메일입니다')
                return
        self.users.append({'name': name, 'email': email, 'phone': phone, 'password': password})
        self._set_status('가입이 완료되었습니다')
        self.reg_name.delete(0, tk.END)
        self.reg_email.delete(0, tk.END)
        self.reg_phone.delete(0, tk.END)
        self.reg_pw.delete(0, tk.END)

    def _login_user(self):
        email = self.login_email.get().strip()
        password = self.login_pw.get().strip()
        for user in self.users:
            if user['email'] == email and user['password'] == password:
                self.current_user = user
                self._set_status(f"{user['name']}님 환영합니다")
                self.user_info.config(text=f"현재 로그인: {user['name']} ({user['email']})")
                self._refresh_bookings()
                return
        self._set_status('로그인 정보를 확인해 주세요')

    def _select_movie(self, _event=None):
        selected = self.movie_table.selection()
        if not selected:
            return
        item_id = selected[0]
        self.selected_movie_id = int(item_id)
        self._draw_seats()

    def _draw_seats(self):
        for widget in self.seat_grid.winfo_children():
            widget.destroy()
        movie = self._movie_by_id(self.selected_movie_id)
        if not movie:
            return
        row_names = ['A', 'B', 'C', 'D']
        col_names = ['1', '2', '3', '4', '5']
        for r, row_name in enumerate(row_names):
            for c, col_name in enumerate(col_names):
                seat_id = f'{row_name}{col_name}'
                taken = movie['seats'][seat_id]
                bg = '#10b981' if not taken else '#ef4444'
                btn = tk.Button(self.seat_grid, text=seat_id, width=6, height=2, bg=bg, fg='white', relief='flat', command=lambda s=seat_id: self._book_seat(s))
                btn.grid(row=r, column=c, padx=4, pady=4)

    def _book_seat(self, seat_id):
        if not self.current_user:
            self._set_status('로그인 후 예매하세요')
            return
        movie = self._movie_by_id(self.selected_movie_id)
        if not movie:
            self._set_status('상영작을 선택해 주세요')
            return
        if movie['seats'][seat_id]:
            self._set_status('이미 선택된 좌석입니다')
            return
        movie['seats'][seat_id] = self.current_user['email']
        booking_id = len(self.bookings) + 1
        self.bookings.append({
            'id': booking_id,
            'user': self.current_user,
            'movie_id': movie['id'],
            'seat': seat_id,
            'status': '예매 완료',
        })
        self._set_status(f"{movie['title']} {seat_id} 좌석이 예매되었습니다")
        self._draw_seats()
        self._refresh_bookings()
        self._refresh_admin()

    def _cancel_booking(self):
        selected = self.booking_table.selection()
        if not selected:
            self._set_status('취소할 예매를 선택해 주세요')
            return
        booking_id = int(selected[0])
        for booking in self.bookings:
            if booking['id'] == booking_id and booking['status'] == '예매 완료':
                movie = self._movie_by_id(booking['movie_id'])
                if movie:
                    movie['seats'][booking['seat']] = ''
                booking['status'] = '취소됨'
                self._set_status('예매가 취소되었습니다')
                break
        self._draw_seats()
        self._refresh_bookings()
        self._refresh_admin()

    def _admin_login(self):
        email = self.admin_email.get().strip()
        pw = self.admin_pw.get().strip()
        if email == 'admin@example.com' and pw == 'admin123':
            self.admin_signed = True
            self.admin_state.config(text='관리자 로그인 완료')
        else:
            self.admin_signed = False
            self.admin_state.config(text='관리자 인증 실패')
        self._refresh_admin()

    def _add_movie_admin(self):
        if not self.admin_signed:
            self.admin_state.config(text='로그인 후 등록 가능합니다')
            return
        title = self.new_title.get().strip()
        show_time = self.new_time.get().strip()
        rating = self.new_rating.get().strip()
        if not title or not show_time or not rating:
            self.admin_state.config(text='모든 정보를 입력해 주세요')
            return
        self._add_movie_entry(title, show_time, rating)
        self.admin_state.config(text='새 상영작이 등록되었습니다')
        self.new_title.delete(0, tk.END)
        self.new_time.delete(0, tk.END)
        self.new_rating.delete(0, tk.END)
        self._refresh_movies()
        self._refresh_admin()

    def _remove_movie(self):
        if not self.admin_signed:
            self.admin_state.config(text='로그인 후 삭제 가능합니다')
            return
        selected = self.admin_movie_table.selection()
        if not selected:
            self.admin_state.config(text='삭제할 상영작을 선택해 주세요')
            return
        movie_id = int(selected[0])
        self.movies = [m for m in self.movies if m['id'] != movie_id]
        for booking in self.bookings:
            if booking['movie_id'] == movie_id and booking['status'] == '예매 완료':
                booking['status'] = '상영 취소'
        self.admin_state.config(text='상영작이 삭제되었습니다')
        if self.selected_movie_id == movie_id:
            self.selected_movie_id = None
            self._draw_seats()
        self._refresh_movies()
        self._refresh_bookings()
        self._refresh_admin()

    def _refresh_movies(self):
        tables = [self.movie_table]
        if hasattr(self, 'admin_movie_table'):
            tables.append(self.admin_movie_table)
        for table in tables:
            for row in table.get_children():
                table.delete(row)
        for movie in self.movies:
            values = (movie['time'], movie['rating'])
            for table in tables:
                table.insert('', 'end', iid=movie['id'], values=values, text=movie['title'])
        self._refresh_titles()

    def _refresh_titles(self):
        tables = [self.movie_table]
        if hasattr(self, 'admin_movie_table'):
            tables.append(self.admin_movie_table)
        for table in tables:
            for item in table.get_children():
                title = self._movie_by_id(int(item))['title']
                table.item(item, text=title)

    def _refresh_bookings(self):
        for row in self.booking_table.get_children():
            self.booking_table.delete(row)
        for booking in self.bookings:
            if self.current_user and booking['user']['email'] == self.current_user['email']:
                movie = self._movie_by_id(booking['movie_id'])
                movie_name = movie['title'] if movie else '삭제된 상영'
                values = (movie_name, booking['seat'], booking['status'])
                self.booking_table.insert('', 'end', iid=booking['id'], values=values)

    def _refresh_admin(self):
        for row in self.admin_booking_table.get_children():
            self.admin_booking_table.delete(row)
        if not self.admin_signed:
            return
        for booking in self.bookings:
            user_name = booking['user']['name']
            movie = self._movie_by_id(booking['movie_id'])
            movie_name = movie['title'] if movie else '삭제된 상영'
            values = (user_name, movie_name, booking['seat'], booking['status'])
            self.admin_booking_table.insert('', 'end', values=values)

    def _movie_by_id(self, movie_id):
        for movie in self.movies:
            if movie['id'] == movie_id:
                return movie
        return None

    def _set_status(self, text):
        self.status.config(text=text)


def main():
    MovieApp()


if __name__ == '__main__':
    main()
