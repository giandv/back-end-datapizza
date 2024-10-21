import React, { useState, useEffect, useRef } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';

function App() {
  const [response, setResponse] = useState([]);
  const [page, setPage] = useState(10);
  // const [data, setData] = useState([]);
  const count = useRef();

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/`)
      .then(response => response.json())
      .then(json => getTenDataFirst(json));
  }, []);

  function getTenDataFirst(data) {
    data.splice(page)
    setResponse(data)
  }

  const handelInfiniteScroll = async () => {
    console.log("scrollHeight" + count.current.scrollHeight);
    console.log("innerHeight" + count.current.innerHeight);
    console.log("scrollTop" + count.current.scrollTop);
  };

  return (
    <div className='flex flex-col w-full justify-center items-center gap-12 py-8 px-4 md:py-16 md:px-12'>
      <div><h1 class=" pt-20 text-4xl font-bold tracking-tight leading-none text-gray-900 sm:text-5xl md:text-6xl dark:text-black text-center">Opportunità</h1><p class="text-gray-500 text-center m-0 text-lg font-medium">Esplora gli annunci, candidati e fai un colloquio con uno dei nostri partners</p></div>
      <div class="flex flex-col gap-12 max-w-5xl w-full">
      <span class="ant-input-group-wrapper ant-input-group-wrapper-lg ant-input-group-wrapper-outlined css-c400bn ant-input-search ant-input-search-large ant-input-search-with-button">
        <span class="ant-input-wrapper ant-input-group css-c400bn">
          <span class="ant-input-affix-wrapper ant-input-affix-wrapper-lg css-c400bn ant-input-outlined">
            <input placeholder="Cerca opportunità" class="ant-input ant-input-lg css-c400bn"
              type="text" value="" />
              <span class="ant-input-suffix">
                <span class="ant-input-clear-icon ant-input-clear-icon-hidden" role="button" tabindex="-1">
                  <span role="img" aria-label="close-circle" class="anticon anticon-close-circle">
</span></span></span></span><span class="ant-input-group-addon"><button type="button" class="bg-accent-100 text-white ant-btn css-dev-only-do-not-override-3ann1w ant-btn-primary ant-btn-lg ant-input-search-button"><span class="px-8">Cerca</span></button></span></span></span>
      </div>
      <div className='flex flex-row flex-wrap gap-4 justify-between' ref={count} onScroll={() => handelInfiniteScroll()}>
          {
            response?.length > 0 && response?.map((data) => {
              return (
                <div class="bg-white p-4 sm:p-6">
                  <div class="sm:flex sm:items-start">
                    <div class="mt-3">
                      <div class="block focus-visible:outline-none rounded-xl  bg-white p-0">
                        <div class="flex items-center gap-3 ">
                          <a class="h-fit w-fit" href="/private/company/epiphany">
                            <img class="object-contain rounded-xl aspect-square w-16"
                              src={data['company']['logo']}
                              alt="Epiphany logo" />
                          </a>
                          <div>
                          <h1 class="m-0 font-bold text-lg">{data['name']}</h1>
                          <p class="m-0 text-sm text-gray-500">
                            <a class="text-gray-500 font-normal underline hover:text-black"
                              href="/private/company/epiphany">{data['company']['name']}</a>
                              • {data['schedule']}
                            </p>
                          </div>
                        </div>
                      </div>
                      <div class="flex flex-col gap-4 mt-6 sm:gap-2">
                        <div class="flex gap-2 flex-wrap">
                        {data['infos'].map((info, index) => {
                          return (
                            <span key={index} class="inline-flex flex-nowrap items-center rounded-md bg-yellow-100 px-2 py-1 text-xs font-medium text-yellow-800">
                              <p class="mb-0">{info['infoname']}</p>
                            </span>
                          );
                        })}
                        {data['technologies'].map((technology, index) => {
                          return (
                            <span key={index} class="inline-flex flex-nowrap items-center rounded-md bg-yellow-100 px-2 py-1 text-xs font-medium text-yellow-800">
                              <p class="mb-0">{technology['skillname']}</p>
                            </span>
                          );
                        })}
                        </div>
                      </div>
                      <div class="mt-6 pb-4">
                        <p class="leading-snug text-gray-600 break-words w-full whitespace-pre-line line-clamp-5">{data['description']}</p>
                      </div>
                    </div>
                  </div>
                  <div key={data['name']}>{data['name']}</div>
                </div>
              )
            })
          }
      </div>
    </div>
  );
}

export default App;
